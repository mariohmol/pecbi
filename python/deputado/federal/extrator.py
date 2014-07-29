# -*- coding: utf-8 -*-
"""
    Extract all data used in calcs
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    
    Running a method for a yer:
    python -m deputado.federal.extrator -m 07 -y 2012 
    
  
    
    
"""

import click,time
from helpers import d, get_file, format_runtime,find_in_df,sql_to_df,read_from_csv,df_to_csv,left_df,to_int,to_number,get_url,to_file




@click.command()
@click.option('-m', '--month', prompt='Month', help='chosse a specific month ex 12',required=False)
@click.option('-y', '--year', prompt='Year', help='chosse a year to run : ex 2014',required=False)
#@click.argument('method', type=click.Path(exists=True))
def main(month,year):
    presenca(month,year)
    

def presenca(month,year):
    for dia in range(1,31):
        data_string=str(dia)+'/'+str(month)+'/'+str(year)
        data_file=str(dia)+'-'+str(month)+'-'+str(year)
        url='http://www.camara.gov.br/sitcamaraws/SessoesReunioes.asmx/ListarPresencasDia?data='+data_string+'&numMatriculaParlamentar=&parteNomeParlamentar=&siglaPartido=&siglaUF='
        print url
        data = get_url(url)
        to_file("presenca/"+data_file+".xml",data)
    

  
        
        
       



                                            
if __name__ == "__main__":
    start = time.time()
    
    total_error=0
    msg_error=[]
    
    main()
    
    print "Total erros found: "+str(total_error)
    print "Erros messages:"
    print     msg_error
    
    
    total_run_time = time.time() - start
    print "Total runtime: " + format_runtime(total_run_time)