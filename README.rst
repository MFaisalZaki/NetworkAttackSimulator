**Status**: Stable release. No extra development is planned, but still being maintained (bug fixes, etc).


Network Attack Simulator
========================

|docs|

Network Attack Simulator (NASim) is a simulated computer network complete with vulnerabilities, scans and exploits designed to be used as a testing environment for AI agents and planning techniques applied to network penetration testing.


Installation
------------

The easiest way to install the latest version of NASim hosted on PyPi is via pip::

  $ pip install nasim


To install dependencies for running the DQN test agent (this is needed to run the demo) run::

  $ pip install nasim[dqn]


To get the latest bleeding edge version and install in development mode see the `Install docs <https://networkattacksimulator.readthedocs.io/en/latest/tutorials/installation.html>`_


Demo
----

To see NASim in action, you can run the provided demo to interact with an environment directly or see a pre-trained AI agent in action.

To run the `tiny` benchmark scenario demo in interactive mode run::

  $ python -m nasim.demo tiny


This will then run an interactive console where the user can see the current state and choose the next action to take. The goal of the scenario is to *compromise* every host with a non-zero value.

See `here <https://networkattacksimulator.readthedocs.io/en/latest/reference/scenarios/benchmark_scenarios.html>`_ for the full list of scenarios.

To run the `tiny` benchmark scenario demo using the pre-trained AI agent, first ensure the DQN dependencies are installed (see *Installation* section above), then run::

  $ python -m nasim.demo tiny -ai


**Note:** Currently you can only run the AI demo for the `tiny` scenario.


Documentation
-------------

The documentation is available at: https://networkattacksimulator.readthedocs.io/



Using with gymnasium
---------------------

NASim implements the `Gymnasium <https://github.com/Farama-Foundation/Gymnasium/tree/main>`_ environment interface and so can be used with any algorithm that is developed for that interface.

See `Starting NASim using gymnasium <https://networkattacksimulator.readthedocs.io/en/latest/tutorials/gym_load.html>`_.


Authors
-------

**Jonathon Schwartz** - Jonathon.schwartz@anu.edu.au


License
-------

`MIT`_ © 2020, Jonathon Schwartz

.. _MIT: LICENSE


What's new
----------

- 2024-11-01 (v 0.12.1) (MAJOR release, WOP)

  - Modified version of NASim based on the paper "Evaluation of Reinforcement Learning for Autonomous Penetration Testing using A3C, Q-learning and DQN" `[Norman Becker et al.] <https://arxiv.org/abs/2407.15656>`_. Please refer to the documentation for further information

  + Addition of Credentials and Vulnerabilities
  + Modifications to existing functions and structures to reflect the intended
  + Modifications to the generator in regards to the new additions
  



- 2023-05-14 (v 0.12.0) (MINOR release)

  + Renamed `NASimEnv.get_minimum_actions -> NASimEnv.get_minumum_hops` to better reflect what it does (thanks @rzvnbr for the suggestion).


- 2023-03-13 (v 0.11.0) (MINOR release)

  + Migrated to `gymnasium (formerly Open AI gym) <https://github.com/Farama-Foundation/Gymnasium/>`_ fromOpen AI gym (thanks @rzvnbr for the suggestion).
  + Fixed bug with action string representation (thanks @rzvnbr for the bug report)
  + Added "sim to real considerations" explanation document to the docs (thanks @Tudyx for the suggestion)

- 2023-02-27 (v 0.10.1) (MICRO release)

  + Fixed bug for host based actions (thanks @nguyen-thanh20 for the bug report)

- 2022-07-30 (v 0.10.0) (MINOR release)

  + Fixed typos (thanks @francescoluciano)
  + Updates to be compatible with latest version of OpenAI gym API (v0.25) (see `Open AI gym API docs <https://www.gymlibrary.ml/content/api/>`_ for details), notable changes include

    * Updated naming convention when initializing environments using the ``gym.make`` API (see `gym load docs <https://networkattacksimulator.readthedocs.io/en/latest/tutorials/gym_load.html>`_ for details.)
    * Updated reset function to match new gym API (shouldn't break any implementations using old API)
    * Updated step function to match new gym API. It now returns two bools, the first specifies if terminal/goal state has been reached and the other specifies if the episode is terminated due to the scenario step limit (if any exists) has been reached. This change may break implementations and you may need to specify (or not) when initializing the gym environment using ``gym.make(env_id, new_step_api=True)``

- 2022-05-19 (v 0.9.1) (MICRO release)

  + Fixed a few bugs and added some tests (thanks @simonsays1980 for the bug reports)

- 2021-12-20 (v 0.9.0) (MINOR release)

  + The value of a host is now observed when any level of access is gained on a host. This makes it so that agents can learn to decide whether to invest time in gaining root access on a host or not, depending on the host's value (thanks @jaromiru for the proposal).
  + Initial observation of reachable hosts now contains the host's address (thanks @jaromiru).
  + Added some support for custom address space bounds in when using scenario generator (thanks @jaromiru for the suggestion).

- 2021-3-15 (v 0.8.0) (MINOR release)

  + Added option of specifying a 'value' for each host when defining a custom network using the .YAML format (thanks @Joe-zsc for the suggestion).
  + Added the 'small-honeypot' scenario to included scenarios.

- 2020-12-24 (v 0.7.5) (MICRO release)

  + Added 'undefined error' to observation to fix issue with initial and later observations being indistinguishable.

- 2020-12-17 (v 0.7.4) (MICRO release)

  + Fixed issues with incorrect observation of host 'value' and 'discovery_value'. Now, when in partially observable mode, the agent will correctly only observe these values on the step that they are recieved.
  + Some other minor code formatting fixes

- 2020-09-23 (v 0.7.3) (MICRO release)

  + Fixed issue with scenario YAML files not being included with PyPi package
  + Added final policy visualisation option to DQN and Q-Learning agents

- 2020-09-20 (v 0.7.2) (MICRO release)

  + Fixed bug with 're-registering' Gym environments when reloading modules
  + Added example implementations of Tabular Q-Learning: `agents/ql_agent.py` and `agents/ql_replay.py`
  + Added `Agents` section to docs, along with other minor doc updates

- 2020-09-20 (v 0.7.1) (MICRO release)

  + Added some scripts for running random benchmarks and describing benchmark scenarios
  + Added some more docs (including for creating custom scenarios) and updated other docs

- 2020-09-20 (v 0.7.0) (MINOR release)

  + Implemented host based firewalls
  + Added priviledge escalation
  + Added a demo script, including a pre-trained agent for the 'tiny' scenario
  + Fix to upper bound calculation (factored in reward for discovering a host)

- 2020-08-02 (v 0.6.0) (MINOR release)

  + Implemented compatibility with gym.make()
  + Updated docs for loading and interactive with NASimEnv
  + Added extra functions to nasim.scenarios to make it easier to load scenarios seperately to a NASimEnv
  + Fixed bug to do with class attributes and creating different scenarios in same python session
  + Fixed up bruteforce agent and tests

- 2020-07-31 (v 0.5.0) (MINOR release)

  + First official release on PyPi
  + Cleaned up dependencies, setup.py, etc and some small fixes


.. |docs| image:: https://readthedocs.org/projects/networkattacksimulator/badge/
    :target: https://networkattacksimulator.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
    :scale: 100%
