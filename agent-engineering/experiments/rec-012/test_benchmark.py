import json
import tempfile
import unittest
from pathlib import Path
from benchmark import bench,load_fixtures, single_actor, manager_workers, merge, ValidationError

HERE=Path(__file__).resolve().parent
class TestREC012(unittest.TestCase):
 def setUp(self):self.tasks=load_fixtures(HERE/'fixtures.json')
 def test_both_topologies_match_all_hand_labelled_cases(self):
  for task in self.tasks:
   for fn in (single_actor,manager_workers):
    with self.subTest(task=task['id'],mode=fn.__name__):
     r=fn(task)
     self.assertEqual(r.status,'completed')
     self.assertEqual(r.output(),task['expected'])
 def test_handoff_fail_closed(self):
  for name in ('logs','impact'):
   for fn in (single_actor, manager_workers):
    with self.subTest(name=name,topology=fn.__name__):
     r=fn(self.tasks[0],(name,'malformed'))
     self.assertEqual(r.status,'failed')
     self.assertTrue(r.error.startswith('invalid-'))
 def test_tool_failures_fail_closed(self):
  for name in ('logs','impact'):
   for fn in (single_actor, manager_workers):
    r=fn(self.tasks[0],(name,'raise'))
    self.assertEqual(r.status,'failed')
    self.assertIn('injected-',r.error)
 def test_timeout_fails_but_does_not_claim_hard_cancellation(self):
  for name in ('logs','impact'):
   for fn in (single_actor, manager_workers):
    r=fn(self.tasks[0],(name,'stall'),timeout_s=.010)
    self.assertEqual(r.status,'failed')
    self.assertEqual(r.error,'time-budget-exceeded')
 def test_type_guards_reject_bool_as_integer(self):
  with self.assertRaises(ValidationError):
   merge({'category':'UI_CRASH','team':'frontend'},{'users':True,'production':True,'sensitive':False})
 def test_result_schema_and_parity(self):
  r=bench(self.tasks,2,.010,'hash')
  self.assertEqual(r['nominal']['single']['n'],len(self.tasks)*2)
  self.assertEqual(r['nominal']['multi']['n'],len(self.tasks)*2)
  self.assertEqual(r['nominal']['single']['outcome_correct'],len(self.tasks)*2)
  self.assertEqual(r['nominal']['multi']['outcome_correct'],len(self.tasks)*2)
  self.assertEqual(r['nominal']['single']['model_calls'],0)
  self.assertEqual(r['nominal']['multi']['total_handoffs'],len(self.tasks)*2*2)
  self.assertEqual(len(r['failures']),6)
if __name__=='__main__':unittest.main()
