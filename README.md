# Restaurant revenue prediction

## Summary

Dans ce notebook, nous allons faire l'analyseexploiratoire des données du projet restaurant revenue prediction.
Ce projet s'inscrit dans le cadre du cours de mlOPS. C'est un projet initié par TFI qui est le propriétaire de beaucoup de chaines de restauration. En effet, avec plus de 1 200 restaurants à service rapide dans le monde, TFI est une société qui possède plusieurs restaurants réputés dans différentes régions d'Europe et d'Asie. Elle emploie plus de 20 000 personnes en Europe et en Asie et investit quotidiennement des sommes importantes dans le développement de nouveaux sites de restauration. Nous avons rencontré quatre types de restaurants différents. Il s'agit des restaurants en ligne, des restaurants mobiles, des drive-thru et des food courts. La décision d'ouvrir un nouveau restaurant est donc difficile à prendre compte tenu de l'émergence de la restauration rapide.
Avec des données subjectives, il est difficile d'extrapoler l'endroit où ouvrir un nouveau restaurant. TF1 a donc besoin d'un modèle qui lui permette d'investir efficacement dans de nouveaux sites de restauration. Ainsi il met a notre disposition un dataset pour  prédire les ventes annuelles de restaurants de 100 000 établissements régionaux.


## Presentation
Lien de la présentation sur Canva
https://www.canva.com/design/DAFsSi4btLI/bS_kbugGOQwD9mr6N2p0qg/edit?utm_content=DAFsSi4btLI&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton


## Lien du deploiement 
``` http://34.135.94.93:5000/predict ```

with body : 

```json
{
    "CityGroup": "Big Cities",
    "Type": "FC",
    "Date": "04/12/2015"
}

```
