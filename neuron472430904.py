'''
Defines a class, Neuron472430904, of neurons from Allen Brain Institute's model 472430904

A demo is available by running:

    python -i mosinit.py
'''
class Neuron472430904:
    def __init__(self, name="Neuron472430904", x=0, y=0, z=0):
        '''Instantiate Neuron472430904.
        
        Parameters:
            x, y, z -- position offset
            
        Note: if name is not specified, Neuron472430904_instance is used instead
        '''
        
        # load the morphology
        from load_swc import load_swc
        load_swc('Ntsr1-Cre_Ai14_GSL_-181184.05.01.01_475124527_m.swc', self,
                 use_axon=False, xshift=x, yshift=y, zshift=z)

        # custom axon (works because dropping axon during import)
        from neuron import h
        self.axon = [h.Section(cell=self, name='axon[0]'),
                     h.Section(cell=self, name='axon[1]')]
        for sec in self.axon:
            sec.L = 30
            sec.diam = 1
            sec.nseg = 1
        self.axon[0].connect(self.soma[0](0.5))
        self.axon[1].connect(self.axon[0](1))
        self.all += self.axon
        
        self._name = name
        self._insert_mechanisms()
        self._discretize_model()
        self._set_mechanism_parameters()
    
    def __str__(self):
        if self._name is not None:
            return self._name
        else:
            return "Neuron472430904_instance"
                
    def _insert_mechanisms(self):
        from neuron import h
        for sec in self.all:
            sec.insert("pas")
        for mech in [u'CaDynamics', u'Ca_HVA', u'Ca_LVA', u'Ih', u'Im_v2', u'K_T', u'Kd', u'Kv2like', u'Kv3_1', u'NaV', u'SK']:
            self.soma[0].insert(mech)
    
    def _set_mechanism_parameters(self):
        from neuron import h
        for sec in self.all:
            sec.Ra = 10.0
            sec.e_pas = -85.2242126465
        for sec in self.apic:
            sec.cm = 1.54
            sec.g_pas = 9.39768054181e-06
        for sec in self.axon:
            sec.cm = 1.0
            sec.g_pas = 0.000760665712443
        for sec in self.dend:
            sec.cm = 1.54
            sec.g_pas = 0.000518771779351
        for sec in self.soma:
            sec.cm = 1.0
            sec.ena = 53.0
            sec.ek = -107.0
            sec.gbar_Ih = 0.000810136
            sec.gbar_NaV = 0.127905
            sec.gbar_Kd = 0.000209484
            sec.gbar_Kv2like = 0.0447338
            sec.gbar_Kv3_1 = 0.0700344
            sec.gbar_K_T = 0.0352815
            sec.gbar_Im_v2 = 0.00410904
            sec.gbar_SK = 0.00216579
            sec.gbar_Ca_HVA = 0.000498632
            sec.gbar_Ca_LVA = 0.000656711
            sec.gamma_CaDynamics = 0.000659798
            sec.decay_CaDynamics = 780.842
            sec.g_pas = 6.20497e-05
    
    def _discretize_model(self):
        for sec in self.all:
            sec.nseg = 1 + 2 * int(sec.L / 40)

