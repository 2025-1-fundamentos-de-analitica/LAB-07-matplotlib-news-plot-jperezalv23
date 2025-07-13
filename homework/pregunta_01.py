# pylint: disable=import-outside-toplevel

import os
import pandas as pd
import matplotlib.pyplot as plt

"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

def pregunta_01():
    """
    Siga las instrucciones del video https://youtu.be/qVdwpxG_JpE para
    generar el archivo `files/plots/news.png`.

    Un ejemplo de la grafica final esta ubicado en la raíz de
    este repo.

    El gráfico debe salvarse al archivo `files/plots/news.png`.
    """

    df = pd.read_csv('files/input/news.csv', index_col=0)
    plt.Figure()

    # Configuración de colores y estilos
    colores = {
        'Internet': 'tab:blue',
        'Newspaper': 'grey',
        'Television': 'dimgray',
        'Radio': 'lightgrey',
    }

    grosores = {
        'Internet': 4,
        'Newspaper': 2,
        'Television': 2,
        'Radio': 2,
    }

    orden_z = {
        'Internet': 2,
        'Newspaper': 1,
        'Television': 1,
        'Radio': 1,
    }

    # Gráficas
    for medio in df.columns:
        plt.plot(
            df[medio],
            color=colores[medio],
            label=medio,
            linewidth=grosores[medio],
            zorder=orden_z[medio]
        )

    plt.title('How people get their news', fontsize=16)
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.axes.get_yaxis().set_visible(False)

    # Anotaciones
    for medio in df.columns:
        inicio = df.index[0]
        fin = df.index[-1]

        for x, año in zip([inicio, fin], [inicio, fin]):
            plt.scatter(
                x=x,
                y=df[medio][año],
                color=colores[medio],
                zorder=orden_z[medio],
            )
            alineacion = 'left' if x == fin else 'right'
            desplazamiento = 0.2 if x == fin else -0.2
            plt.text(
                x + desplazamiento,
                df[medio][año],
                f"{medio} {df[medio][año]}%",
                ha=alineacion,
                va='center',
                color=colores[medio],
            )

    # Guardar resultado
    plt.tight_layout()
    os.makedirs('files/plots', exist_ok=True)
    plt.savefig('files/plots/news.png')
