class CalculationMemory:

    def __init__(self):
        self.undo_stack = []
        self.redo_stack = []

    def save_state(self, state):
        self.undo_stack.append(state.copy())
        self.redo_stack.clear()

    def undo(self):
        if len(self.undo_stack) == 0:
            return None

        if len(self.undo_stack) == 1:
            return self.undo_stack[-1]

        self.redo_stack.append(self.undo_stack.pop())

        return self.undo_stack[-1]

    def redo(self):
        if not self.redo_stack:
            return None

        state = self.redo_stack.pop()
        self.undo_stack.append(state)

        return state