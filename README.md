# diagram_as_code_python

<br>

> **Note:** Declarative diagramming involves the creation of diagrams through a declarative approach, encompassing a range from flowcharts to organization charts. In this methodology, users define the relationships and logic of the diagram's elements using a formal language, as opposed to the traditional method of manually placing and connecting shapes on a canvas.
>
> While this approach may not be the most practical for sporadically generating individual diagrams, it proves highly advantageous for automation processes reliant on reusable templates and their seamless customization.

<br>

## Technologies used
- **Diagram-As-Code**
- **Python 3**
- **Linux**
  
<br>



## 1. 

<img width="1269" alt="Screenshot 2023-11-28 at 18 11 30" src="https://github.com/otam-mato/diagram_as_code_python/assets/113034133/03998a26-d776-4dd6-bbdf-6e1d31a90796">

<br><br>

```python3
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
```

## Prerequisites

- **Python 3** installed.
- **pip** installed.
- **pip install diagrams**


## Steps:

### 1. Create the deployment of V1 of the app

- **[Download the manifest 'deployment_app_v1.yml'](https://github.com/otam-mato/nodejs_mysql_web_app_kubernetes/blob/66874767022185dcf7c7eae0c8bc2967ec60dcea/deployment_app_v1.yml)**

- **Apply it**:

```yml
kubectl apply -f deployment_app_v1.yaml
```
