import json
import os


def lw(event, context):
    
    print("i m Vimal Daga from my World i m dev  ")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! from LW by VD  dev dev ')
    }

