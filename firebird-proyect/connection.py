from firebird.driver import connect, driver_config

def create_connection_db(user,pwd,role):
    #Ubicacion del servidor de FireBird
    driver_config.server_defaults.host.value = 'localhost'

    #Usuario FireBird
    driver_config.server_defaults.user.value = user

    #Clave FireBird
    driver_config.server_defaults.password.value = pwd
    
    #PC1
    connection = connect('C:\\Users\\PC1\\Desktop\\proyects\\DbsFlameRobin\\MAXDETALLESPORFACTURATIPOB.FDB'
                        ,role=role)
    
    #PC2
    #connection = connect('C:\\Users\\Santi\\Documents\\DBd-FlameRobin\\MAXDETALLESPORFACTURA.FDB')

    return connection