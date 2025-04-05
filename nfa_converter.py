from pyformlang.regular_expression import Regex
import graphviz


def regex_to_nfa(regex_str):
    """Convert regex to epsilon-NFA using pyformlang"""
    regex = Regex(regex_str)
    return regex.to_epsilon_nfa()


def draw_nfa(automaton, filename="nfa"):
    """Draw the NFA with Graphviz and correctly display ε for epsilon transitions"""
    dot = graphviz.Digraph(format='png')
    dot.attr(rankdir='LR')

    for state in automaton.states:
        shape = "doublecircle" if state in automaton.final_states else "circle"
        dot.node(str(state), shape=shape)

    for start_state in automaton.start_states:
        dot.node("", shape="none")
        dot.edge("", str(start_state))

    for transition in automaton._transition_function.get_edges():
        from_state = str(transition[0])
        symbol = "ε" if transition[1].value is None else str(transition[1].value)  # Show ε for epsilon
        to_state = str(transition[2])
        dot.edge(from_state, to_state, label=symbol)

    return dot.render(filename, cleanup=True)
