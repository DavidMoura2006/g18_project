from flask import render_template, session
from classes.machine import Machine
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import matplotlib as mpl
import io
import base64


def apps_plot():
    engine = create_engine(f'sqlite:///{filename}factorys.db')
    df_products = pd.read_sql_table('Machine', engine)
    
    result = df_products.groupby('machines_type').size()
    print(result.head())
    
    p_ids = result.index
    p_names = []
    for p_id in p_ids:
        p_obj = Machine.obj.get(p_id)
        if p_obj:
            p_names.append(p_obj.machines_type)
        else:
            p_names.append(str(p_id))  

    quantities = result.values

    mpl.rcParams.update({
        'axes.edgecolor': 'white',
        'axes.labelcolor': 'white',
        'xtick.color': 'white',
        'ytick.color': 'white',
        'text.color': 'white',
        'axes.titlesize': 18,      
        'axes.labelsize': 14,       
        'xtick.labelsize': 12,      
        'ytick.labelsize': 12,
        'font.family': 'sans-serif',
        'font.sans-serif': ['Arial']
    })

    fig, ax = plt.subplots(figsize=(10, 6))  

    fig.patch.set_facecolor('#2c2c2c')
    ax.set_facecolor('#2c2c2c')

    ax.bar(p_names, quantities, width=0.5, color='#FFD700', edgecolor='black')

    ax.set_xlabel('Tipo de Máquina')
    ax.set_ylabel('Número de Máquinas')
    ax.set_title('Número de Máquinas por tipo')
    plt.xticks(rotation=15)

    fig.subplots_adjust(left=0.08, right=0.97, top=0.90, bottom=0.25)

    buf = io.BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', facecolor=fig.get_facecolor())
    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')
    plt.close(fig)

    return render_template("plot.html", image=image, ulogin=session.get("user"))

















