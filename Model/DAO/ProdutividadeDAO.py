# coding: utf-8
from datetime import date

class ProdutividadeDAO:

    @staticmethod
    # def enviar_emailDAO(self, anexo1, chamados_atendidos, chamados_n_atendidos, emails, emails_copias, total):
    def enviar_emailDAO(dados):

        def criar_mostrar_data():
            hoje = date.today()
            dia = hoje.day
            mes = hoje.month
            ano = hoje.year
            data_ = "%.2d/%.2d/%d" % (dia, mes, ano)
            return data_

        data = criar_mostrar_data()
        import win32com.client
        const=win32com.client.constants
        olMailItem = 0x0
        obj = win32com.client.Dispatch("Outlook.Application")
        newMail = obj.CreateItem(olMailItem)
        newMail.Subject = "ACOMPANHAMENTO CHAMADOS FILA INSTALAÇÃO/SISTEMAS - " + data
        # newMail.Body = "I AM\nTHE BODY MESSAGE!"
        newMail.BodyFormat = 2 # olFormatHTML https://msdn.microsoft.com/en-us/library/office/aa219371(v=office.11).aspx
        total_atendidos = str(dados.Total)
        chamados = str(dados.ChamadosAtendidos)
        newMail.HTMLBody = "<HTML><BODY><p style='font-family:Consolas;font-size:14'>" \
                             "Segue abaixo dados de produtividade"  \
                             "<br>      " \
                             "<br>   Chamados atendidos" \
                             "<br>     <br>" + chamados + "   " \
                             "<br>Total de " + total_atendidos + " chamados     <br>   " \
                             "<br> Chamados não atendidos<br>" + dados.ChamadosNaoAtendidos +"<br>" \
                             "<br><img src='C:\\PUBMOVE\\assinatura2.png'></BODY></HTML>"


        newMail.To = dados.Emails
        newMail.CC = dados.EmailsCopias

        if dados.Anexo1 == True:
            attachment1 = r"C:\Rel_Diario\Não atendidos.xlsx"
            newMail.Attachments.Add(Source=attachment1)
        newMail.display()
