import os


def save_graph_as_png(graph, filename=None):
    if filename is None:
        filename = os.path.splitext(os.path.basename(__file__))[0]

    png_bytes = graph.get_graph().draw_mermaid_png()
    with open(f"{filename}.png", "wb") as f:
        f.write(png_bytes)
