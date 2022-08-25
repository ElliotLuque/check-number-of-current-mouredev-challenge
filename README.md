# Número de retos en total (MoureDev 2022)


[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Integration%20Test/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)

Esta pequeña acción devuelve el número de **[retos de programación de MoureDev](https://retosdeprogramacion.com/semanales2022)**

Puedes recogerlo como output para la entrada de otra acción y, por ejemplo, calcular el número de retos que llevas completados

## Uso

### Workflow de ejemplo

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@master
    
    - name: Check total
      uses: ElliotLuque/check-total-mouredev-challenges@v1.1
```

### Outputs

| Output                                             | Descripción                                        |
|------------------------------------------------------|-----------------------------------------------|
| `totalChallenges`  | Número de retos en total    |

## Ejemplos

Restando el total menos los retos completados, conseguiríamos el número de retos que nos faltan

```yaml
steps:
  - name: Checkout
    uses: actions/checkout@v3

  - name: Count done challenges
    id: done
    run: ls src/main/java/com/elliot/retos | wc -l

  - name: Count number of challenges
    id: total
    uses: ElliotLuque/check-total-mouredev-challenges@v1.1

  - name: Calculate remaining
    run: echo "${{ steps.total.outputs.totalChallenges }} - ${{ steps.done.outputs.doneChallenges }}"
      
```
