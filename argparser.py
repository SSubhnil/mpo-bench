import argparse


def add_bool_arg(parser, name, default=False):
    """
    Adds a boolean argument to the parser
    :param parser: (ArgumentParser) the parser the arguments should be added to
    :param name: (str) name of the argument
    :param default: (bool) default value of the argument
    """
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument('--' + name, dest=name, action='store_true')
    group.add_argument('--no-' + name, dest=name, action='store_false')
    parser.set_defaults(**{name: default})


def parse():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description='Implementation of MPO on gym environments')

    parser.add_argument(
        '--env', type=str, default='Pendulum-v0',
        help='gym environment')
    parser.add_argument(
        '--load', type=str, default=None,
        help='loading path if given')

    # train params - general
    add_bool_arg(parser, 'train', default=True)
    add_bool_arg(parser, 'render', default=False)
    parser.add_argument(
        '--log_dir', type=str, default=None,
        help='log directory')

    # train parameters
    parser.add_argument(
        '--policy_evaluation', type=str, default='td',
        help='policy evalution method')
    parser.add_argument(
        '--eps', type=float, default=0.1,
        help='hard constraint of the E-step')
    parser.add_argument(
        '--eps_mean', type=float, default=0.1,
        help='hard constraint on C_mu')
    parser.add_argument(
        '--eps_sigma', type=float, default=1e-4,
        help='hard constraint on C_Sigma')
    parser.add_argument(
        '--gamma', type=float, default=0.99,
        help='learning rate')
    parser.add_argument(
        '--alpha', type=float, default=10,
        help='scaling factor of the lagrangian multiplier in the M-step')
    parser.add_argument(
        '--sample_episode_num', type=int, default=30,
        help='number of episodes to learn')
    parser.add_argument(
        '--sample_episode_maxlen', type=int, default=200,
        help='length of an episode (number of training steps)')
    parser.add_argument(
        '--sample_action_num', type=int, default=64,
        help='number of sampled actions')
    parser.add_argument(
        '--backward_length', type=int, default=0,
        help='trajectory backward length')
    parser.add_argument(
        '--rerun_num', type=int, default=5,
        help='number of reruns of the mini batch')
    parser.add_argument(
        '--mb_size', type=int, default=64,
        help='size of the mini batch')
    parser.add_argument(
        '--lagrange_iteration_num', type=int, default=5,
        help='number of optimization steps of the Lagrangian')
    parser.add_argument(
        '--iteration_num', type=int, default=1000,
        help='number of iteration to learn')
    parser.add_argument(
        '--save_path', type=str, default='mpo_model.pt',
        help='saving path if save flag is set')

    # eval params (default at false)
    add_bool_arg(parser, 'eval', default=False)
    parser.add_argument(
        '--eval_episodes', type=int, default=100,
        help='number of episodes for evaluation')
    parser.add_argument(
        '--eval_ep_length', type=int, default=3000,
        help='length of an evaluation episode')

    return parser.parse_args()
