from enp.core.network import ENPNetwork

topology = {
    "neurons": ["A", "B"],
    "connections": {("A", "B"): 0.5}
}

net = ENPNetwork(topology)
inputs = {"A": 1.2}  # estimula o neurônio A

for t in range(10):
    output = net.step(inputs)
    print(f"Step {t} -> Output: {output}")
    inputs = output  # realimentação