.. _scenario_generation_explanation:

Scenario Generation Explanation
===============================

Generating the scenarios involves a number of design decisions that strongly determine the form of the network being generated. This document aims to explain some of the more technical details of generating the scenarios when using the :ref:`scenario_generator` class.

The scenario generator is based heavily on prior work, specifically:

- `Sarraute, Carlos, Olivier Buffet, and Jörg Hoffmann. "POMDPs make better hackers: Accounting for uncertainty in penetration testing." Twenty-Sixth AAAI Conference on Artificial Intelligence. 2012. <https://www.aaai.org/ocs/index.php/AAAI/AAAI12/paper/viewPaper/4996>`_
- `Speicher, Patrick, et al. "Towards Automated Network Mitigation Analysis (extended)." arXiv preprint arXiv:1705.05088 (2017). <https://arxiv.org/abs/1705.05088>`_

Network Topology
----------------

Description to come. Till then we recommend reading the papers linked above, especially the appendix of Speicher et al (2017).

.. _correlated_configurations:

Correlated Configurations
-------------------------

When generating a scenario with ``uniform=False`` the scenario will be generated with host configurations being correlated. This means that rather than the OS and services it is running being chosen uniformly at random from the available OSs and services, they are chosen randomly with increased probability given to OSs and services that are being run by other hosts whose configuration was generated earlier.


Specifically, the distribution of configurations of each host in the network are generated using a Nested Dirichlet Process, so that across the network hosts will have corelated configurations (i.e. certain services/configurations will be more common across hosts on the network). The correlation can be controlled using three parameters: ``alpha_H``, ``alpha_V``, and ``lambda_V``.

``alpha_H`` and ``alpha_V`` control the degree of correlation, with lower values leading to greater correlation.

``lambda_V`` controls the average number of services running per host, with higher values will mean more services (so more vulnerable) hosts on average.

All three parameters must have a positive value, with the defaults being ``alpha_H=2.0``, ``alpha_V=2.0``, and ``lambda_V=1.0``, which tends to generate networks with fairly correlated configurations where hosts have only a single vulnerability on average.


.. _generated_exploit_probs:

Generated Exploit Probabilities
-------------------------------

Success probabilities of each exploit are determined based on the value of the ``exploit_probs`` argument, as follows:

- ``exploit_probs=None`` - probabilities generated randomly from uniform distribution over the interval (0, 1).
- ``exploit_probs=float`` - probability of each exploit is set to the float value, which must be a valid probability.
- ``exploit_probs=list[float]`` - probability of each exploit is set to corresponding float value in list. This requires that the length of the list matches the number of exploits as specified by the ``num_exploits`` argument.
- ``exploit_probs="mixed"`` - probabilities chosen from a set distribution which is based on the `CVSS attack complexity <https://www.first.org/cvss/v2/guide>`_ distribution of `top 10 vulnerabilities in 2017 <https://go.recordedfuture.com/hubfs/reports/cta-2018-0327.pdf>`_. Specifically, exploit probabilities are chosen from [0.3, 0.6, 0.9] which correspond to high, medium and low attack complexity, respectively, with probabilities [0.2, 0.4, 0.4].

For deterministic exploits set ``exploit_probs=1.0``.


Firewall
--------

The firewall restricts which services can be communicated with between hosts on different subnets. This is mostly done by selecting services at random to block between each subnet, with some contraints.

Firstly, there exists no firewall between subnets in the user zone. So communication between hosts on different user subnets is allowed for all services.

Secondly, the number of services blocked is controlled by the ``restrictiveness`` parameter. This controls the number of services to block between zones (i.e. between the internet, DMZ, sensitive, and user zones).

Thirdly, to ensure that the goal can be reached, traffic from at least one service running on each subnet will be allowed between each zone. This may mean more services will be allowed than restrictiveness parameter.


Credentials (Optional)
----------------------

To include credentials the following arguments are introduced:

- ``num_cred=0`` - represents the number of credentials used. (max. of 9)

- ``wiretapping_cost=0`` - cost to wiretap a target

In general every exploit can be used with each credential, each exploit is generated with every possible credential as an input. These permutations are handled as one exploit to not affect the ``num_exploits=None`` variable.

**Distribution**: Each credentials only has singular source to be discovered on. They are randomly handed to each subnet and then further distributed to the hosts in each subnet. 

Since every Host is vulnerable to at least one exploit, the credentials are placed in the ``credentials_tofind`` variable of the host and can be found by ``Wiretapping()``.

**Locking**: Following the distribution the hosts are potentionaly locked. For this a random order to visit each host is generated and an array of ``found_credentials`` is being tracked.

Each visited host is locked with a random already 'found' credential (if possible), credentials saved in ``credentials_tofind`` are noted for future use.

**Limitations**: 'Distribution' and 'Locking' are simple representations of the potential applications.

- Both are fully random and not influenced by ``seed`` or ``restrictiveness``

- credentials found by ``PrivelegeEscalation()`` are not represented nor implemented

- 'Locking' does not uniformally 'lock' existing hosts, resulting in a random density of this property


Vulnerabilities (Optional)
--------------------------

- ``num_vul=0`` - number of vulnerabilities

- ``vul_scan_cost=0`` - cost to scan a host for vulnerabilities

Similiar to the depiction of how vulnerabilities work, each one is linked to a service. The exploits utilizing these vulnerabilities are not bound to a OS and have a ``prob=1``.

Hosts running a 'vulnerable' service also get the vulnerability alocated to them to ensure susceptibility.

**Limitations**: Vulnerabilities are randomly bound to services and not additionally to OS's, making it less diverse in terms of permutations.

Furthermore, the possibility of a service with a linked vulnerability running on a host without the vulnerability is not present.