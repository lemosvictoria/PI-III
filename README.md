# Projeto Integrador III - Centro Universitário IESB

Introdução: Projeto acadêmico de Análise de Dados, utilizando Power BI para analisar o comportamento das eleições no Brasil através da rede social Twitter.

## Tweet Scrapper

Script desenvolvido para buscar tweets envolvendo os principais candidatos a presidência do Brasil nas eleições de 2022. Para recuperar as postagens, o script usa o projeto [twint](https://github.com/kevctae/twint) e, para realizar alguns ajustes no retorno, utiliza a biblioteca [pandas](https://pandas.pydata.org/docs/).

Para usar o script, instale primeiro as dependências:

```sh
pip install -r tweet_scrapper/requirements.txt
```

Use o seguinte comando para retornar os tweets das últimas horas:

```sh
python ./tweet_scrapper/tweet_scrapper.py <termo de busca> <quantidade de horas> <pasta para gravar a saída>
```

Caso queira criar um cronjob para rodar o script periodicamente a cada hora, a seguinte regra é sugerida:

```sh
0 * * * * python ./tweet_scrapper/tweet_scrapper.py <termo de busca> 1 <pasta para gravar a saída> >>  <pasta para gravar os logs>/<termo de busca>.log 2>&1
```


<br>
Desenvolvedores:
<p align="justify"> :octocat: <a href="https://github.com/IsabelaPinheiro"> Isabela Pinheiro - 1922130015 </a> </p>
<p align="justify"> :octocat: <a href="https://github.com/SillasReis"> Sillas Reis - 1822130004 </a> </p>
<p align="justify"> :octocat: <a href="https://github.com/lemosvictoria"> Victória Lemos - 1812130070 </a> </p>
