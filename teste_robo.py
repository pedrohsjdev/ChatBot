import unittest
from robo import *

class TesteSaudacoes(unittest.TestCase):

    def setUp(self):
        self.robo = ChatBot("Robô de Atendimento do Cubo Mágico",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])  

    def test_oi_ola_tudo_bem(self):
        print("test case for 'oi', 'olá' and 'tudo bem?' messages")

        greetings = ["oi", "olá", "tudo bem?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("olá, sou o robô de atendimento do cubo mágico", answer.text.lower())

    def test_bom_dia_tarde_noite(self):
        print("test case for 'bom dia', 'boa tarde' and 'boa noite' messages")

        greetings = ["bom dia", "boa tarde", "boa noite"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn(greeting + ", sou o robô de atendimento do cubo mágico.", answer.text.lower()) 

class TesteInformacoes(unittest.TestCase):

    def setUp(self):
        self.robo = ChatBot("Robô de Atendimento do Cubo Mágico",
                   read_only=True,
                   statement_comparison_function=comparar_mensagens,     
                   logic_adapters=[
                       {
                           "import_path": "chatterbot.logic.BestMatch"
                       }
                   ])  

    def test_o_que_e(self):
        print("test case for 'o que é o cubo mágico?' message")

        greetings = ["o que é o cubo mágico?", "cubo mágico", "cubo magico é um brinquedo?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("cubo de rubik, também conhecido como cubo mágico, é um quebra-cabeça tridimensional", answer.text.lower())


    def test_quem_criou(self):
        print("test case for 'quem criou o cubo mágico?' message")

        greetings = ["quem criou o cubo magico?", "quem inventou o cubo magico?", "de onde surgiu o cubo magico?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("o cubo mágico foi criado pelo professor de arquitetura ernő rubik", answer.text.lower())


    def test_como_montar(self):
        print("test case for 'como montar o cubo mágico?' message")

        greetings = ["como montar um cubo magico?", "como resolver o cubo magico?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("o cubo mágico permite ser resolvido de diversas formas, a mais fácil para iniciantes é o metodo básico", answer.text.lower())


    def test_quem_consegue_montar(self):
        print("test case for 'qualquer um consegue montar o cubo mágico?' message")

        greetings = ["qualquer um consegue montar o cubo mágico?", "eu consigo montar um cubo mágico?", "é possível montar um cubo magico?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("sim. o cubo mágico pode ser resolvido por qualquer pessoa", answer.text.lower())

    def test_diferentes_precos(self):
        print("test case for 'existe diferença entre um cubo magico barato e um caro?' message")

        greetings = ["existe diferença entre um cubo magico barato e um caro?", "existe cubo magico barato?", "porque um cubo mágico é tão caro?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("hoje em dia existem uma infinidade de modelos de cubo magico", answer.text.lower())

    
    def test_qual_record(self):
        print("test case for 'qual o record do cubo mágico?' message")

        greetings = ["qual o menor tempo que o cubo magico foi resolvido?", "qual o record do cubo mágico?", "qual menor tempo do cubo mágico?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("os records só podem ser validos se acontecerem em campeonatos oficiais", answer.text.lower())

    
    def test_onde_comprar(self):
        print("test case for 'onde comprar um cubo mágico?' message")

        greetings = ["onde comprar um cubo mágico?", "como comprar um cubo mágico?", "onde encontrar um cubo mágico?"]
        for greeting in greetings:
            print(f"testing: {greeting}")

            answer = self.robo.get_response(greeting)
            self.assertIn("o cubo mágico tradicional pode ser facilmente encontrado em qualquer loja de brinquedos ou quebra cabeças", answer.text.lower())

    

if __name__ == "__main__":
    loader = unittest.TestLoader()
    tests = unittest.TestSuite()

    tests.addTest(loader.loadTestsFromTestCase(TesteSaudacoes))
    tests.addTest(loader.loadTestsFromTestCase(TesteInformacoes))

    executer = unittest.TextTestRunner()
    executer.run(tests)