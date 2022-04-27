from mongoengine import register_connection, connect


def global_init():
    register_connection(alias='core',
                        name='ClusterUnit01',
                        host='mongodb+srv://admin:<1346795>@clusterunit01.ngqrj.mongodb.net/ClusterUnit01?retryWrites=true&w=majority',
                        port='27017')
    connect(host='mongodb+srv://admin:<1346795>@clusterunit01.ngqrj.mongodb.net/ClusterUnit01?retryWrites=true&w=majority')
