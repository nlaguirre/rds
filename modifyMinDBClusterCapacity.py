import boto3
import datetime

def lambda_handler(event, context):
    client = boto3.client('rds')
    lowermincapacity = 2 # Set min capacity for low traffic
    lowermincapacityhour = '23' # Set lower min capacity at XX GTM
    uppermincapacity = 8 # # Set min capacity for high traffic
    uppermincapacityhour = '10' # Set upper min capacity at XX GTM
    clusterid = 'testdatabase'
    currenthour = datetime.datetime.now().strftime("%H")

    if lowermincapacityhour == currenthour:
        mincapacity = lowermincapacity
        print("Son las ", currenthour, " hs. La cantidad de ACUs a configurar es: ",mincapacity)
    elif uppermincapacityhour == currenthour:
        mincapacity = uppermincapacity
        print("Son las ", currenthour, " hs. La cantidad de ACUs a configurar es: ",mincapacity)
    else:
        print("Son las ", currenthour, " hs. No se realizará ningún cambio.")
        return
    
    response = client.modify_db_cluster(
        DBClusterIdentifier=clusterid, 
        ScalingConfiguration={
            'MinCapacity': mincapacity
        }
    )
