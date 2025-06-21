from langgraph.graph import StateGraph, START, END
from lg_utility import save_graph_as_png
from typing import TypedDict


# Global list of strings named 'warehouse' with 10 hardcoded items
cricket_warehouse = [
    "gloves",
    "pads",
    "shoes",
    "helmet",
    "jersey",
    "bat",
    "ball",
    "stumps"
]


class State(TypedDict):
    value: str
    add_to_cart: bool
    check_stock: bool
    payment: bool
    out_of_stock: bool
    cancel_order: bool
    message: str
    route: str


def initialize_state_defaults(state: dict):
    return {
        "value": state.get("value", 0),
        "add_to_cart": None,
        "check_stock": False,
        "payment": False,
        "out_of_stock": False,
        "cancel_order": False,
        "route": None,
        "message": None
    }


def route_validator(state: State):
    retval = state["route"]

    return retval


def add_to_cart(state: State):
    print(f"Checking for availability of item {state['value']} in warehouse")

    return state


def check_stock(state: State):
    if state["value"] in cricket_warehouse:
        state["check_stock"] = True
        print(f"Item {state['value']} available..")
        state["route"] = "available"
    else:
        state["check_stock"] = False
        print(f"Item {state['value']} out of stock...")
        state["route"] = "out_of_stock"
    return state


def payment(state: State):
    print("Payment Received!!!")
    state["payment"] = True

    return state


def out_of_stock(state: State):
    state["out_of_stock"] = True
    return state


def cancel_order(state: State):
    state["cancel_order"] = True
    return state


def message(state: State):
    if state["payment"]:
        state["message"] = "Order Placed!!!"
    elif state["cancel_order"]:
        state["message"] = "Order Cancelled!!!"
    elif state["out_of_stock"]:
        state["message"] = "Out of stock!!!"
    else:
        state["message"] = "Server unavailable"

    return state


def build_graph():
    builder = StateGraph(State)

    builder.add_node("INITIALIZER", initialize_state_defaults)
    builder.add_node("Add_to_cart", add_to_cart)
    builder.add_node("Check_stock", check_stock)
    builder.add_node("Payment", payment)
    builder.add_node("Out_of_stock", out_of_stock)
    builder.add_node("Cancel_order", cancel_order)
    builder.add_node("Message", message)

    builder.add_edge(START, "INITIALIZER")
    builder.add_edge("INITIALIZER", "Add_to_cart")
    builder.add_edge("Add_to_cart", "Check_stock")
    builder.add_conditional_edges(
        "Check_stock",
        route_validator, {
            "available": "Payment",
            "out_of_stock": "Out_of_stock"
        }
    )

    builder.add_edge("Payment", "Message")
    builder.add_edge("Out_of_stock", "Cancel_order")
    builder.add_edge("Cancel_order", "Message")
    builder.add_edge("Message", END)

    graph = builder.compile()

    save_graph_as_png(graph, __file__)

    return graph


graph = build_graph()


def main():
    response = graph.invoke({"value": "bat"})
    print(f"Response :{response['message']}")
    print()

    response = graph.invoke({"value": "bowling_arm"})
    print(f"Response :{response['message']}")
    print()


if __name__ == "__main__":
    main()
