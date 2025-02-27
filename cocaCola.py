class ProcessoProducaoBebida:
    def produzir(self):
        self.misturar_ingredientes()
        self.adicionar_sabor()
        self.regular_acucar()
        self.embalar()
        self.armazenar()

    def misturar_ingredientes(self):
        print("Misturando ingredientes base (água, gás, etc.)")

    def adicionar_sabor(self):
        pass 

    def regular_acucar(self):
        print("Ajustando nível de açúcar")

    def embalar(self):
        print("Envasando bebida em garrafas")

    def armazenar(self):
        print("Armazenando as garrafas")

class CocaCola(ProcessoProducaoBebida):
    def adicionar_sabor(self):
        print("Adicionando sabor de cola")

class Fanta(ProcessoProducaoBebida):
    def adicionar_sabor(self):
        print("Adicionando sabor de laranja")

class Sprite(ProcessoProducaoBebida):
    def adicionar_sabor(self):
        print("Adicionando sabor de limão")

coca_cola = CocaCola()
coca_cola.produzir()

fanta = Fanta()
fanta.produzir()

sprite = Sprite()
sprite.produzir()
