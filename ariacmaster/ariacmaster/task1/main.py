from world.state import WorldState
import world.tree as bt
import py_trees
import time

WORLD = WorldState()
def tick_tree(tree, delay=0.5):
    """Tick the tree and display the state."""
    while tree.status != py_trees.common.Status.SUCCESS:
        WORLD.tick_count += 1
        print(f"\n{'─'*60}")
        print(f"TICK {WORLD.tick_count}")
        print(f"{'─'*60}")
        # Show WORLD state BEFORE tick
        print(f"WORLD: {WORLD}")
        tree.tick_once()

        # Show tree state AFTER tick
        print(f"\nTree Status: {tree.status}")
        print(py_trees.display.unicode_tree(root=tree, show_status=True))

        if delay > 0:
            time.sleep(delay)

if __name__ == "__main__":
    tree = bt.create()

    # Keep initialized conditions

    # Run until lane change completes
    tick_tree(tree)
