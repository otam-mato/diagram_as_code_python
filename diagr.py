from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS
from diagrams.aws.database import ElastiCache, RDS
from diagrams.aws.network import ELB
from diagrams.aws.network import Route53

with Diagram("ECS Clustered Services", show=False, direction="TB", graph_attr={"labelloc": "t"}):
    dns = Route53("AWS Route53")
    lb = ELB("AWS ELB")

    with Cluster("ECS cluster"):
        svc_group = [ECS("web1"),
                     ECS("web2"),
                     ECS("web3")]

    with Cluster("AWS RDS Cluster"):
        db_primary = RDS("RDS")
        db_primary - [RDS("RDS ReadOnly")]

    memcached = ElastiCache("AWS ElastiCache")

    dns >> lb >> svc_group
    svc_group >> db_primary
    svc_group >> memcached
