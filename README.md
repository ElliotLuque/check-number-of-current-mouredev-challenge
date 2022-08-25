# Número total de retos (MoureDev 2022)

![status-badge]

Esta pequeña action devuelve el número de **[retos de programación semanales 2022 de MoureDev](https://retosdeprogramacion.com/semanales2022)**

Puedes recogerlo como output para la entrada de otra acción y, por ejemplo, calcular el número de retos que llevas completados.

## Uso

### Workflow de ejemplo

```yaml
name: My Workflow
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    # Al darle una ID a la action puedes recoger su valor de salida con ${{ steps.ID_PASO.outputs.NOMBRE_OUTPUT }}
    # El nombre del output debe ser el definido en la tabla de abajo
    - name: Check total challenges
      id: outputTotal
      uses: ElliotLuque/check-total-mouredev-challenges@v1.1
```

### Outputs

| Output                                             | Descripción                                        |
|------------------------------------------------------|-----------------------------------------------|
| `totalChallenges`  | Número de retos en total    |

## Ejemplos

Restando el total menos los retos completados, conseguiríamos el número de retos que nos faltan.

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

Para mi repositorio personal de retos, he usado esta action junto a **[DynamicBadges](https://github.com/marketplace/actions/dynamic-badges)** para crear una badge con el progreso de mis retos (cambia de color mediante avances).

![example-challenge-badge]

```yaml
steps:
  - name: Checkout
    uses: actions/checkout@v3

  - name: Count done challenges
    id: done
    run: echo "::set-output name=doneChallenges::$(ls src/main/java/com/elliot/retos | wc -l)"

  - name: Count total challenges
    id: total
    uses: ElliotLuque/check-total-mouredev-challenges@v1.1

  - name: Calculate color of badge
    id: color
    run: >- 
      echo "::set-output name=progressColor::$(
      num=${{ steps.done.outputs.doneChallenges }}
      max=${{ steps.total.outputs.totalChallenges }}

      let percentage='(num*100) / max'

      case $percentage in

          100) echo "brightgreen" ;;
          ([7-9][5-9]) echo "green" ;;
          ([5-7][0-9]) echo "yellow" ;;
          ([2-5][5-9]) echo "orange" ;;
          * ) echo "lightgray" ;;

      esac
      )"

  - name: Generate badge from gist
    uses: schneegans/dynamic-badges-action@v1.4.0
    with:
      auth: ${{ secrets.GIST_SECRET }}
      gistID: 877b28319e86c7acc17d3116177a6a04
      filename: badge.json
      label: challenges
      message: ${{ steps.done.outputs.doneChallenges }} / ${{ steps.total.outputs.totalChallenges }}
      color: ${{ steps.color.outputs.progressColor }}
```

[status-badge]: https://img.shields.io/github/workflow/status/ElliotLuque/check-total-mouredev-challenges/Integration%20Test?label=Integration%20Test
[example-challenge-badge]: https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/ElliotLuque/877b28319e86c7acc17d3116177a6a04/raw/badge.json

## Ver también

- **[Repositorio personal de retos semanales 2022](https://github.com/ElliotLuque/retos-java-2022)**

- **[Action usada para generar badges a partir de un JSON](https://github.com/marketplace/actions/dynamic-badges)**
