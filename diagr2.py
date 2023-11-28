from diagrams import Cluster, Diagram
from diagrams.aws.compute import ECS, EKS, Lambda
from diagrams.aws.database import Redshift
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3

with Diagram("Event Processing", show=False, graph_attr={"labelloc": "t"}):
    source = EKS("EKS source")

    with Cluster("Event Flows"):
        with Cluster("Event Workers"):
            workers = [ECS("service1"),
                       ECS("service2"),
                       ECS("service3")]

        queue = SQS("AWS SQS event queue")

        with Cluster("Processing"):
            handlers = [Lambda("process1"),
                        Lambda("process2"),
                        Lambda("process3")]

    store = S3("S3")
    dw = Redshift("Redshift")

    source >> workers >> queue >> handlers
    handlers >> store
    handlers >> dw
