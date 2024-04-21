import unittest
from maze import Maze
from graphics import Window

class Test(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_cols,num_rows,10,10,win=Window(120,120))
        self.assertEqual(len(m1._cells),num_cols)
        self.assertEqual(len(m1._cells[0],num_rows))
    def test_maze_break_entrace_and_exit(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0,0,num_cols,num_rows,10,10,win=Window(120,120))
        self.assertEqual(m1._cells[5][8].has_top_wall,False)
        self.assertEqual(m1._cells[num_cols-3][num_rows-3].has_bottom_wall,False)

    def test_maze_reset_cells_visted(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell.visited,
                    False,
                )      

if __name__ == '__main__':
    unittest.main()        


