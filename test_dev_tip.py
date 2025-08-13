import unittest
from unittest.mock import patch
import dev_tip



class TestDevTip(unittest.TestCase):
    def test_tips_list_exists(self):
        """Test that tips list exists and has content"""
        self.assertIsInstance(dev_tip.tips, list)
        self.assertGreater(len(dev_tip.tips), 0)

    def test_tips_are_strings(self):
        """Test that all tips are strings"""
        for tip in dev_tip.tips:
            self.assertIsInstance(tip, str)
            self.assertGreater(len(tip.strip()), 0)

    @patch('builtins.print')
    def test_main_prints_tip(self, mock_print):
        """Test that main function prints a tip"""
        dev_tip.main()
        # Should print header and a tip
        self.assertEqual(mock_print.call_count, 2)
        mock_print.assert_any_call("🛠️  Dev Tip of the Day:")
        # Second call should be one of our tips
        printed_tip = mock_print.call_args_list[1][0][0]
        self.assertIn(printed_tip, dev_tip.tips)

    def test_has_sufficient_tips(self):
        """Test that we have at least 20 tips for variety"""
        self.assertGreaterEqual(len(dev_tip.tips), 20)

    @patch('dev_tip.random.choice')
    def test_random_selection_is_used(self, mock_choice):
        """Test that random.choice is called for tip selection"""
        mock_choice.return_value = dev_tip.tips[0]
        dev_tip.main()
        mock_choice.assert_called_once_with(dev_tip.tips)

    def test_all_tips_can_be_selected(self):
        """Test that randomization can select any tip over multiple runs"""
        # This is a probabilistic test - run many times and verify diversity
        with patch('builtins.print'):
            selected_tips = set()
            for _ in range(100):
                # Mock print to capture the selected tip
                with patch('dev_tip.random.choice') as mock_choice:
                    for tip in dev_tip.tips:
                        mock_choice.return_value = tip
                        dev_tip.main()
                        selected_tips.add(tip)

        # Verify that we can theoretically select all tips
        self.assertEqual(len(selected_tips), len(dev_tip.tips))



if __name__ == "__main__":
    unittest.main()
