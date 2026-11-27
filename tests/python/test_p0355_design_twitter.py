from itertools import product
import unittest

from python.p0355_design_twitter import Twitter


class TwitterGlobalLogOracleTests(unittest.TestCase):
    def apply(self, instance, posts, relationships, command):
        name, arguments = command
        expected = None
        if name == 'postTweet':
            posts.append(arguments)
        elif name == 'follow':
            if arguments not in relationships:
                relationships.append(arguments)
        elif name == 'unfollow':
            if arguments in relationships:
                relationships.remove(arguments)
        else:
            reader = arguments[0]
            expected = []
            for author, tweet_id in reversed(posts):
                if author == reader or (reader, author) in relationships:
                    expected.append(tweet_id)
                    if len(expected) == 10:
                        break
        result = getattr(instance, name)(*arguments)
        self.assertIs(type(result), list if name == 'getNewsFeed' else type(None))
        self.assertEqual(result, expected)

    def test_all_short_mutation_sequences_against_global_post_log(self):
        operations = (('postTweet', (1,)), ('postTweet', (2,)),
                      ('follow', (1, 2)), ('follow', (2, 1)),
                      ('unfollow', (1, 2)), ('unfollow', (2, 1)))
        sequences = 0
        for length in range(6):
            for commands in product(operations, repeat=length):
                instance, posts, relationships = Twitter(), [], []
                for reader in (1, 2, 3):
                    self.apply(instance, posts, relationships, ('getNewsFeed', (reader,)))
                for index, (name, arguments) in enumerate(commands):
                    if name == 'postTweet':
                        arguments += (10000 - index,)
                    self.apply(instance, posts, relationships, (name, arguments))
                    for reader in (1, 2, 3):
                        self.apply(instance, posts, relationships, ('getNewsFeed', (reader,)))
                sequences += 1
        self.assertEqual(sequences, 9331)

    def test_exact_30000_calls_all_users_and_follow_changes(self):
        commands = [('postTweet', (tweet_id % 500 + 1, tweet_id))
                    for tweet_id in range(10001)]
        commands += [('follow', (1, author)) for author in range(2, 501)]
        for _ in range(4875):
            commands += [('getNewsFeed', (1,)), ('unfollow', (1, 500)),
                         ('getNewsFeed', (1,)), ('follow', (1, 500))]
        self.assertEqual(len(commands), 30000)
        instance, posts, relationships = Twitter(), [], []
        for command in commands:
            self.apply(instance, posts, relationships, command)


if __name__ == '__main__':
    unittest.main()
