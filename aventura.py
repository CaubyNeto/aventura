nome = input("Digite seu nome: ")
print(f"Bem-vindo, {nome}, para essa aventura!")

resposta = input("Você está em uma estrada de terra, ela chegou ao fim e você pode ir para a esquerda ou para a direita. Qual caminho você gostaria de seguir? ").lower()
if resposta == "esquerda":
    resposta = input("Você chega a um rio, pode contorná-lo ou atravessá-lo a nado? Digite contornar para contornar e nadar para nadar: ").lower()
    if resposta == "nadar":
        print("Você nada e foi comido por um jacaré")
    elif resposta == "contornar":
        print("Você caminhou muitos quilômetros, ficou sem água e perdeu o jogo.")
    else:
        print("Não é uma opção válida. Você perdeu!")
elif resposta == "direita":
    resposta = input("Você chega a uma ponte, ela parece mal-estruturada, você quer atravessá-la ou voltar (atravessar/voltar)? ")
    if resposta == "voltar":
        print("Você voltou e perdeu.")
    elif resposta == "atravessar":
        resposta = input("Você atravessou a ponte e se encontrou com um grupo de estranhos. Você quer conversar com eles (sim/não)? ")
        if resposta == "sim":
            resposta = input("Você fala com os estranhos e eles querem te ajudar. Você quer a ajuda deles (sim/não)? ")
            if resposta == "sim":
                print("Você foi ajudado pelos estranhos e está seguro agora. Você GANHOU!")
            elif resposta == "não":
                print("Os estranhos o ignoraram e você não foi ajudado. Você perdeu!")
            else:
                print("Não é uma opção válida. Você perdeu!")
        elif resposta == "não":
            print("Você ignorou os estranhos e eles ficaram ofendidos e você perdeu.")
        else:
            print("Não é uma opção válida. Você perdeu!")
    else:
        print("Não é uma opção válida. Você perdeu!")
else:
    print("Não é uma opção válida. Você perdeu!")    
print(f"Obrigado por jogar, {nome}.")
