import json
import logging
import os
from decimal import Decimal

import boto3
from botocore.config import Config
import src.utilities.formataCampos as Fc

from logging.config import fileConfig

from datetime import datetime

fileConfig(os.path.join(os.path.dirname(__file__), 'src/configuration/logger_config.ini')) # noqa
logger = logging.getLogger('root')


def lambda_handler(event, context):
    logger.debug(event)
    msg_success = "Sucesso, total de registros inseridos na base:"

    try:
        dynamodb = boto3.resource(
            'dynamodb',
            config=Config(
                region_name='sa-east-1',
                signature_version='v4',
                retries={
                    'max_attempts': 5,
                    'mode': 'standard'
                }
            )
        )

        table = dynamodb.Table('tbpp8132_sald_rese_plno_prea')
        itens = []

        date_hour_start = datetime.now()

        for ret in event:
            message = ret["payload"]["value"]
            payload = json.loads(message)
            obj = payload["saldos_previdencia"]
            itens.append(
                {
                    'txt_objt_prod_plno_prea':
                        Fc.formataProdutoPlano(obj['codigo_produto_previdencia'],  # noqa
                                               obj['numero_plano_previdencia']),  # noqa
                    'txt_objt_cobt_prsa_prea':
                        Fc.formataCoberturaProvisao(obj["tipo_cobertura"],
                                                    obj["codigo_cobertura"],
                                                    obj["provisao"]),  # noqa
                    'num_digt_plno_prea': int(obj['dac_plano_previdencia']),
                    'num_docm_pati_plno_prea':
                        Fc.formataCpf(obj['numero_cpf'],
                                      obj['dac_cpf']),
                    'cod_cont_debt_plno_prea':
                        Fc.formataConta(obj['banco'],
                                        obj['numero_agencia'],
                                        obj['numero_conta_corrente'],
                                        obj['digito_verificador_conta']),
                    'cod_situ_plno': obj['status_plano']['codigo_status_plano'],  # noqa
                    'des_situ_plno': obj['status_plano']['descricao_status_plano'],  # noqa
                    'cod_situ_rese': obj['status_reserva']['codigo_status_reserva'],  # noqa
                    'des_situ_rese': obj['status_reserva']['descricao_status_reserva'],  # noqa
                    'cod_tipo_trib_plno': obj['tributacao']['codigo_tributacao'],  # noqa
                    'des_tipo_trib_plno': obj['tributacao']['descricao_codigo_tributacao'],  # noqa
                    'nom_prod_prea': obj['nome_produto'],
                    'nom_prao_prsa': obj['nome_provisao'],
                    'vlr_sald_rese_pati': Decimal(str(obj['saldo_participante'])),  # noqa
                    'vlr_sald_rese_empr': Decimal(str(obj['saldo_empresa'])),
                    'vlr_prmi_pati': Decimal(str(obj['premio_participante'])),  # noqa
                    'vlr_prmi_empr': Decimal(str(obj['premio_empresa'])),
                    'qtd_cota_pati': Decimal(str(obj['quantidade_cotas_participante'])),  # noqa
                    'qtd_cota_empr': Decimal(str(obj['quantidade_cotas_empresa'])),  # noqa
                    'vlr_pndt_psst_rese_pati': Decimal(str(obj['valor_nao_proc_participante'])),  # noqa
                    'vlr_pndt_psst_rese_empr': Decimal(str(obj['valor_nao_proc_empresa'])),  # noqa
                    'vlr_rese_gard_pati': Decimal(str(obj['saldo_garantido_participante'])),  # noqa
                    'vlr_rese_gard_empr': Decimal(str(obj['saldo_garantido_empresa'])),  # noqa
                    'vlr_excd_finn_pati_1': Decimal(str(obj['exc_financeiro_1_participante'])),  # noqa
                    'vlr_excd_finn_empr_1': Decimal(str(obj['exc_financeiro_1_empresa'])),  # noqa
                    'vlr_excd_finn_pati_2': Decimal(str(obj['exc_financeiro_2_participante'])),  # noqa
                    'vlr_excd_finn_empr_2': Decimal(str(obj['exc_financeiro_2_empresa'])),  # noqa
                    'vlr_excd_finn_pati_3': Decimal(str(obj['exc_financeiro_3_participante'])),  # noqa
                    'vlr_excd_finn_empr_3': Decimal(str(obj['exc_financeiro_3_empresa'])),  # noqa
                    'dat_hor_atui_sald_rese': obj['data_hora_processamento'],  # noqa
                    'txt_objt_regr_visu_sald_rese': {
                        'cod_regr_visu_rese_cana_asns': obj['bloqueio_visualizacao']['tipo_bloqueio_bkl'],  # noqa
                        'des_regr_visu_rese_cana_asns': obj['bloqueio_visualizacao']['desc_tipo_bloqueio_bkl'],  # noqa
                        'cod_regr_visu_rese_caix_elet': obj['bloqueio_visualizacao']['tipo_bloqueio_cxa'],  # noqa
                        'des_regr_visu_rese_caix_elet': obj['bloqueio_visualizacao']['desc_tipo_bloqueio_cxa']}  # noqa
                }
            )
        with table.batch_writer() as batch:
            for item in itens:
                batch.put_item(Item=item)

        date_hour_finish = datetime.now()

        duration_in_seconds = (date_hour_start-date_hour_finish).total_seconds() # noqa

        logger.info("Execução realiazada com sucesso", extra={"processados": len(itens), # noqa
                                                              "data_hora_inicio": date_hour_start, # noqa
                                                              "data_hora_conclusao": date_hour_finish, # noqa
                                                              "duracao": abs(duration_in_seconds)}) # noqa

        return json.dumps(msg_success + str(len(itens)))  # noqa

    except Exception as ex:
        msg = \
            f"Uma exceção ocorreu ao processar o evento: " \
            f"{event} \nContexto: {context} \n" \
            f"Exceção: {ex}"

        subject = "Erro Convivência saldo previdência"

        sns_topic = os.environ['SNS_TOPIC_NAME']
        sns = boto3.client(
            'sns',
            config=Config(
                region_name='sa-east-1',
                signature_version='v4',
                retries={
                    'max_attempts': 5,
                    'mode': 'standard'
                }
            )
        )
        print("SNS_TOPIC: " + sns_topic)
        response = sns.publish(
            TopicArn=sns_topic,
            Subject=subject,
            Message=msg
        )

        print(response)

        logger.error(msg)

        retorno = {
            "message": "O Processamento do evento falhou",
            "result": "NOK",
            "statusCode": "400"
        }

        return json.dumps(retorno)

# locals()['lambda_handler'](value, 'saldos_previdencia')
