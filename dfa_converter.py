from pyformlang.regular_expression import Regex
import graphviz


def regex_to_dfa(regex_str):
    """Convert regex to DFA (via NFA without epsilon transitions)"""
    regex = Regex(regex_str)
    epsilon_free_nfa = regex.to_epsilon_nfa().remove_epsilon_transitions()
    dfa = epsilon_free_nfa.to_deterministic()
    return dfa


def draw_dfa(automaton, filename="dfa"):
    """Draw the DFA with renamed states"""
    dot = graphviz.Digraph(format='png')
    dot.attr(rankdir='LR')

    state_mapping = {state: f"q{idx}" for idx, state in enumerate(automaton.states)}

    for state in automaton.states:
        shape = "doublecircle" if state in automaton.final_states else "circle"
        dot.node(state_mapping[state], shape=shape)

    for start_state in automaton.start_states:
        dot.node("", shape="none")
        dot.edge("", state_mapping[start_state])

    for from_state, symbol, to_state in automaton._transition_function.get_edges():
        dot.edge(state_mapping[from_state], state_mapping[to_state], label=str(symbol))

    return dot.render(filename, cleanup=True)
