print("== Programa do Desconto ==")
valorProduto = float( input("Valor do produto: ") )
taxaDesconto = float( input("Taxa de Desconto: ") )

valorDesconto = valorProduto * (taxaDesconto / 100)
valorComDesconto = valorProduto - valorDesconto

print("Valor do desconto: R$", valorDesconto)
print("Valor do produto com desconto: R$", valorComDesconto)