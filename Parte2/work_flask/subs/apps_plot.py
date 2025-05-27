from flask import render_template, session
from classes.machine import Machine
from datafile import filename

import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import io
import base64


def apps_plot():
    engine = create_engine(f'sqlite:///{filename}factorys.db')
    df_products = pd.read_sql_table('Machine', engine)  #alterado
    result = df_products.groupby('machines_type')['capacity'].sum() #alterado
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

    fig, ax = plt.subplots()
    plt.bar(p_names, quantities, width=0.4, label='machines_type')  #alterado
    x_index = range(len(p_names))
    plt.xticks(x_index, labels=p_names)
    plt.xlabel('machines_type')  #alterado
    plt.ylabel('Capacity')  #alterado
    plt.title('Machines Capacities')  #alterado
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image = base64.b64encode(buf.getvalue()).decode('utf-8')

    return render_template("plot.html", image=image, ulogin=session.get("user"))



















