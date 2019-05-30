# coding: utf-8
# def enviar_email_produtividade(anexo1, chamados_atendidos, chamados_n_atendidos, emails, emails_copias,total):

from Model.DTO.ProdutividadeDTO import ProdutividadeDTO
from Model.DAO.ProdutividadeDAO import ProdutividadeDAO

class ProdutividadeCTR:
    @staticmethod
    def email_produtividade(anexo1_CTR, chamados_atendidos_CTR, chamados_n_atendidos_CTR, emails_CTR,
                            emails_copias_CTR, total_CTR):

        produtividadeDTO = ProdutividadeDTO
        produtividadeDTO.Anexo1 = anexo1_CTR
        produtividadeDTO.ChamadosAtendidos = chamados_atendidos_CTR
        produtividadeDTO.ChamadosNaoAtendidos = chamados_n_atendidos_CTR
        produtividadeDTO.Emails = emails_CTR
        produtividadeDTO.EmailsCopias = emails_copias_CTR
        produtividadeDTO.Total = total_CTR

        produtividadeDAO = ProdutividadeDAO
        produtividadeDAO.enviar_emailDAO(produtividadeDTO)