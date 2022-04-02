compra = float(input('Valor da compra? R$'))
qtd_parcelas = int(input('Quantas parcelas? R$'))
p_juros = float(input('Juros por parcela? R$'))

parcela_sj = compra / qtd_parcelas
v_juros = parcela_sj * p_juros/100
parcela_cj = parcela_sj + v_juros

print('Valor final da parcela = R$ %.2f' % parcela_cj)
print('Valor do juros = R$ %.2f' % v_juros)
print('Valor final da compra = R$ %.2f' % (parcela_cj * qtd_parcelas))
