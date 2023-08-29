class Cliente:
    def __init__(self, pCpf, pNome, pTelefone, pCpfIndicador = None):
        self.FCpf = pCpf
        self.FNome = pNome
        self.FTelefone = pTelefone
        self.FCpfIndicador = pCpfIndicador

class Conta:
    def __init__(self, pNumeroAgencia, pNumeroConta, pCpfCliente):
        self.FNumeroAgencia = pNumeroAgencia
        self.FNumeroConta = pNumeroConta
        self.FCpfCliente = pCpfCliente

class Agencia:
    def __init__(self, pNumero, pEndereco):
        self.FNumero = pNumero
        self.FEndereco = pEndereco   
        self.FClientes = []
        self.FContas = []   

    def CadastrarClientes(self, pCpf, pNome, pTelefone, pCpfIndicador = None):
        vCliente = Cliente(pCpf, pNome, pTelefone, pCpfIndicador)
        self.FClientes.append(vCliente)

    def CadastrarConta(self, pNumeroConta, pCpfCliente):
        vConta = Conta(self.FNumero, pNumeroConta, pCpfCliente)
        self.FContas.append(vConta)

    def ListarContas(self):
        for vConta in self.FContas:
            for vCliente in self.FClientes:
                if vCliente.FCpf != vConta.FCpfCliente:
                    continue
                
                print(f"Número da agência: {self.FNumero}, Número da conta: {vConta.FNumeroConta}, Nome do cliente: {vCliente.FNome}")

    def ListarClientes(self):
        for vCliente in self.FClientes:
            print(f"Nome: {vCliente.FNome}, Telefone: {vCliente.FTelefone}")

    def ListarClientesIndicados(self):
        for vCliente in self.FClientes:
            if vCliente.FCpfIndicador:
                print(f"Nome: {vCliente.FNome}, Telefone: {vCliente.FTelefone}, Indicado por (CPF): {vCliente.FCpfIndicador}")

class Banco:
    def __init__(self):
        self.FAgencias = []

    def CadastrarAgencia(self, pNumero, pEndereco):
        vAgencia = Agencia(pNumero, pEndereco)
        self.FAgencias.append(vAgencia)
        return vAgencia

    def ListarContasPorAgencia(self, pNumAgencia):
        for vAgencia in self.FAgencias:
            if vAgencia.FNumero != pNumAgencia:
                continue
            
            vAgencia.ListarContas()

    def ListarContasPorCliente(self, pCpfCliente):
        for vAgencia in self.FAgencias:
            for vCliente in vAgencia.FClientes:
                if vCliente.FCpf != pCpfCliente:
                    continue

                for vConta in vAgencia.FContas:
                        if vConta.FCpfCliente != pCpfCliente:
                            continue
                        
                        print(f"Número da agência: {vAgencia.FNumero}, Número da conta: {vConta.FNumeroConta}")

    def ListarClientesPorAgencia(self, pNumAgencia):
        for vAgencia in self.FAgencias:
            if vAgencia.FNumero == pNumAgencia:
                vAgencia.ListarClientes()

    def ListarClientesIndicados(self):
        for vAgencia in self.FAgencias:
            vAgencia.ListarClientesIndicados()

def Main():
    vBanco = Banco()
    while True: 
        Menu()
        vResposta = input('Escolha uma opção: ').strip()

        if vResposta == '0':
            break

        elif vResposta == '1':
            CadastrarAgencia(vBanco)

        elif vResposta == '2':
            CadastrarCliente(vBanco)  
        
        elif vResposta == '3':
            CadastrarConta(vBanco)

        elif vResposta == '4':
            ConsultarContasPorAgencia(vBanco)

        elif vResposta == '5':
            ConsultarContasPorCliente(vBanco)  
        
        elif vResposta == '6':
            ConsultarClientesPorAgencia(vBanco)  
        
        elif vResposta == '7':
            ConsultarClientesIndicados(vBanco)    

        else:
            vResposta = input('Escolha uma opção existente: ')  

def Menu():
    print("Menu:")
    print("1. Cadastrar Agência")
    print("2. Cadastrar Cliente")
    print("3. Cadastrar Conta")
    print("4. Consultar Contas (por Agência)")
    print("5. Consultar Contas (por Cliente)")
    print("6. Consultar Clientes (por Agência)")
    print("7. Consultar Clientes (Indicados)")
    print("0. Sair")

def CadastrarAgencia(pBanco: Banco):
    vNumeroAgencia = input('\nQual o número da Agência: ') # Validar Numero Inteiro
    vEnderecoAgencia = input('Qual o endereço da Agência: ')

    pBanco.CadastrarAgencia(vNumeroAgencia, vEnderecoAgencia)
    print('Agência Cadastrada com Sucesso!!\n')
    print(f'Número da Agência: {vNumeroAgencia}, Endereço: {vEnderecoAgencia}')

def CadastrarCliente(pBanco: Banco):
    vNumAgencia = input('Informe o numero sua agência: ')
    vPossuiAgencia = False

    for vAgencia in pBanco.FAgencias:
        if vAgencia.FNumero != vNumAgencia:
            continue
        
        vPossuiAgencia = True
        vCpf = input('\nQual o CPF do Cliente: ')
        vNome = input('Qual o Nome do Cliente: ')
        vTelefone = input('Qual o Telefone do Cliente: ') 
        vPossuiIndicador = input('Foi Indicado? S/N \n')

        if vPossuiIndicador.lower() == 's':
            vIndicador = input('\nQual o CPF do Indicador: ')

            # Validar Cpf Indicador
            
            vAgencia.CadastrarClientes(vCpf, vNome, vTelefone, vIndicador)
            print('Cliente Cadastrado com Sucesso!!\n')
            print(f'CPF: {vCpf}, Nome: {vNome}, Telefone: {vTelefone}, Indicador: {vIndicador}')
        else:
            vAgencia.CadastrarClientes(vCpf, vNome, vTelefone)
            print('Cliente Cadastrado com Sucesso!!\n')
            print(f'CPF: {vCpf}, Nome: {vNome}, Telefone: {vTelefone}')
    
    if not vPossuiAgencia:
        print(f'Não foi encontrado a Agência: {vNumAgencia}, tente novamente...\n')

def CadastrarConta(pBanco: Banco):
    vNumAgencia = input('\nInforme o número da Agência: ')
    vAgenciaEncontrada = None

    for vAgencia in pBanco.FAgencias:
        if vAgencia.FNumero == vNumAgencia:
            vAgenciaEncontrada = vAgencia
            break
    
    if vAgenciaEncontrada is None:
        print('Agência não encontrada.')
        return

    vCpfCliente = input('\nInforme o CPF do Cliente: ')
    vClienteEncontrado = None

    for vCliente in vAgenciaEncontrada.FClientes:
        if vCliente.FCpf == vCpfCliente:
            vClienteEncontrado = vCliente
            break
    
    if vClienteEncontrado is None:
        print('CPF do Cliente não encontrado na agência.')
        return

    vNumConta = input('\nInforme o número da Conta: ')
    vAgenciaEncontrada.CadastrarConta(vNumConta, vCpfCliente)
    print('Conta cadastrada com sucesso!\n')
    print(f'Número da Agência: {vNumAgencia}, Endereço: {vAgenciaEncontrada.FEndereco}')

def ConsultarContasPorAgencia(pBanco: Banco):
    vNumAgencia = input('\nInforme o número da Agência: ')
    vPossuiAgencia = False

    for vAgencia in pBanco.FAgencias:
        if vAgencia.FNumero != vNumAgencia:
            continue

        vPossuiAgencia = True
        vAgencia.ListarContas()
    
    if not vPossuiAgencia:
        print(f"\nNão foi encontrada a Agência: {vNumAgencia}, verifique...")

def ConsultarContasPorCliente(pBanco: Banco):
    vCpfCliente = input('\nInforme o CPF do Cliente: ')
    pBanco.ListarContasPorCliente(vCpfCliente)

def ConsultarClientesPorAgencia(pBanco: Banco):
    vNumAgencia = input('\nInforme o número da Agência: ')
    pBanco.ListarClientesPorAgencia(vNumAgencia)

def ConsultarClientesIndicados(pBanco: Banco):
    pBanco.ListarClientesIndicados()

Main()