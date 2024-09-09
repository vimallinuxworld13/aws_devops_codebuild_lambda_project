import json
import os


def lw(event, context):
    
    print("i m Vimal Daga from my World i m dev  final test ")
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda! from LW by VD  final test and bye  ')
    }

