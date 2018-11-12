# -*- coding: utf-8 -*-
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================


"""Module with the functionality related to inference methods.
"""

import inferpy as inf


INF_METHODS = ["KLpq", "KLqp", "Laplace", "ReparameterizationEntropyKLqp", "ReparameterizationKLKLqp", "ReparameterizationKLqp", "ScoreEntropyKLqp", "ScoreKLKLqp", "ScoreKLqp", "ScoreRBKLqp", "WakeSleep", "MetropolisHastings"]
""" List with all the alowed implemented inference methods """


INF_METHODS_ALIAS = {"Variational" : "KLqp", "MCMC":"MetropolisHastings"}
""" Aliases for some of the inference methods """



class Inference(object):
    def run(self):
        pass   #make obstract



class Variational(Inference):
    pass


class MCMC(Inference):
    pass




### later on, remove this class and make dynamic the definition
class KLqp(Variational):
    def __init__(self, P=None, Q=None):

        if Q == None and P != None:
            self.Q = inf.Qmodel.build_from_pmodel(P)
        elif Q != None and P == None:
            self.Q = Q
        else:
            raise ValueError("P or Q must be defined, but not both")

        self.Q = Q
















