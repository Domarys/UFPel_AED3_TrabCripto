# UFPel_AED3_TrabCripto (créditos da questão: Prof Ricardo Matsumura)
Repositório contém os arquivos usados como solução de força bruta do Trabalho 2 de Criptografia da disciplina de Algoritmos e Estruturas de Dados 3 da UFPel.


Um importante texto contendo ideias liberais perigosas foi encontrado, porém (supresa!) criptografado. 
Sua tarefa como criptoanalista do governo é encontrar o texto original, fornecer seu conteúdo e sua opinião pessoal sobre o tema tratado. 
Seu predecessor fez alguns avanços antes de desaparecer misteriosamente e abaixo estão suas anotações que esperamos poder ajudá-lo. 
Precisamos que vários criptoanalistas quebrem de forma independente para garantir que o texto recuperado está correto. 
Como incentivo, vocês receberão bônus no salário em ordem de solução: o primeiro criptoanalista a quebrar o código receberá o maior bônus, 
seguido do segundo e assim por diante. Precisamos destes resultados impreterivelmente até o dia 20 de junho de 2019, ao meio-dia.


--- anotações recuperadas do diário de trabalho do Criptoanalista #42 ---



01/05/2019, 13h45
- O texto está contido no arquivo "cipher_text.enc", que foi certamente criptografado utilizando AES, muito provavelmente 
com chave de 256 bits, que chamarei de CHAVE1, e codificado em base64. Indicações de que o aplicativo "openssl" foi utilizado. 
á tentei todos nomes de cachorros conhecidos e datas de nascimento possíveis. Deixei um cluster tentando abrir o arquivo por força bruta, 
sem sucesso até agora, indicando que a senha é bastante grande e aleatória. Não posso deixar meus colegas descobrirem o que já descobri.



02/05/2019, 07h15
- O arquivo "cipher_pass.enc" parece conter a CHAVE1. Porém, o arquivo foi criptogrado utilizando uma chave pública RSA. 
Felizmente a chave pública também foi obtida pelos espiões e ela não parece ser muito longa, talvez seja possível quebrá-la! Vou iniciar 
amanhã. Agora preciso aumentar a segurança de minha sala. Sinto que estou sendo observado.



03/05/2019, 14h00
- O arquivo "cipher_pub.enc" contém a chave pública RSA, mas o arquivo também foi criptografado utilizando AES, com uma 
chave desconhecida que chamarei de CHAVE2. Por que ninguém usa mais DES? Minha vida seria mais fácil. 



03/05/2019, 23h40
Um de nossos analistas de TI obteve a hash da CHAVE2 em um servidor e gentilmente me informou, em troca de alguns presentes 
no Pokemon Go. O maldito quer pegar minha gym do escritório. Por aceitá-lo como amigo no Facebook ele ainda me garantiu que a senha é apenas 
composta de números e letras. A hash é "YTEUCxI8/wSjrTpm/EqL7s9aR++fqs2f3JBav3vK5Uk=" e parece ser uma hash SHA256. É o mesmo algoritmo de 
hash utilizado pelo Bitcoin. Me pergunto se isso significa algo. Agora só preciso quebrar este arquivo para obter a chave pública e quebrar 
esta para obter a chave original! Pelo tamanho da hash, estimo que a senha não pode ter mais de 8 caracteres. Finalmente alguma sorte! 
Preciso de mais recursos, porém. Creio que terei que paralelizar com meus colegas esta tarefa. Farei isso tão logo verifique quem está 
tentando destrancar minha porta...


--- fim das anotações ---

