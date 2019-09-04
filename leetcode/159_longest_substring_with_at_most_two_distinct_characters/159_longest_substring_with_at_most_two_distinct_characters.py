class Solution(object):
  def longest_distinct_substring(self, s):
    current_substring = []
    longest_substring = []
    distinct_char_count = 0
    most_recent_char_idx = {}
    for c in s:
      current_chars = list(most_recent_char_idx)
      if c not in current_chars:
        if distinct_char_count >= 2:
          char_to_remove = current_substring[0]
          char_to_remove_idx = most_recent_char_idx[char_to_remove]

          for key in current_chars:
            if most_recent_char_idx[key] <= char_to_remove_idx:
              distinct_char_count -= 1
              del most_recent_char_idx[key]
            else:
              most_recent_char_idx[key] -= char_to_remove_idx + 1

          current_substring = current_substring[char_to_remove_idx + 1:]

        distinct_char_count += 1

      current_substring.append(c)
      if len(current_substring) > len(longest_substring):
        longest_substring = current_substring[:]
      most_recent_char_idx[c] = len(current_substring) - 1

    return "".join(longest_substring)