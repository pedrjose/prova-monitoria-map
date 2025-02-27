class ProcessoCompra:
    def realizar_compra(self):
        self.selecionar_produto()
        self.selecionar_pagamento()
        self.selecionar_envio()
        self.finalizar_compra()

    def selecionar_produto(self):
        print("Produto selecionado")

    def selecionar_pagamento(self):
        pass  

    def selecionar_envio(self):
        pass  

    def finalizar_compra(self):
        print("Compra finalizada, preparando para envio.")

class CompraCartaoCredito(ProcessoCompra):
    def selecionar_pagamento(self):
        print("Pagamento com cartão de crédito aprovado")

class CompraBoleto(ProcessoCompra):
    def selecionar_pagamento(self):
        print("Pagamento com boleto gerado")

class EnvioNormal(ProcessoCompra):
    def selecionar_envio(self):
        print("Escolhendo envio normal: Entrega em 7 dias úteis")

class EnvioExpresso(ProcessoCompra):
    def selecionar_envio(self):
        print("Escolhendo envio expresso: Entrega em 1-2 dias úteis")

compra_cartao_envio_normal = CompraCartaoCredito()
compra_cartao_envio_normal.selecionar_envio = EnvioNormal().selecionar_envio
compra_cartao_envio_normal.realizar_compra()

compra_boleto_envio_express = CompraBoleto()
compra_boleto_envio_express.selecionar_envio = EnvioExpresso().selecionar_envio
compra_boleto_envio_express.realizar_compra()
