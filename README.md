# Número del reto de la semana (MoureDev 2022)


[![Actions Status](https://github.com/jacobtomlinson/python-container-action/workflows/Integration%20Test/badge.svg)](https://github.com/jacobtomlinson/python-container-action/actions)

Esta pequeña acción devuelve el número del reto de la semana actual de los **[retos de programación de MoureDev](https://retosdeprogramacion.com/semanales2022)**

Puedes recogerlo como output para la entrada de otra acción y, por ejemplo, calcular el número de retos que llevas completados con los totales

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
    
    - name: Run action
      uses: ElliotLuque/check-number-of-current-mouredev-challenge@v1
```

### Outputs

| Output                                             | Descripción                                        |
|------------------------------------------------------|-----------------------------------------------|
| `challengeNumber`  | Número del reto de la semana actual    |

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
    uses: ElliotLuque/check-number-of-current-mouredev-challenge@v1

  - name: Calculate remaining
    run: echo "${{ steps.done.outputs.challengeNumber }} - ${{ steps.total.outputs.doneChallenges }}"
      
```
