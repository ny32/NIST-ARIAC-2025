import world.tree as bt
import py_trees
import time
from world.context import WORLD

def tick_tree(tree, _world, delay=0.5):
    """Tick the tree and display the state."""
    while tree.status != py_trees.common.Status.SUCCESS:
        _world.tick_count += 1
        print(f"\n{'─'*60}")
        print(f"TICK {_world.tick_count}")
        print(f"{'─'*60}")
        # Show WORLD state BEFORE tick
        
        print(_world)
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
    tick_tree(tree, WORLD, delay=0.5)
