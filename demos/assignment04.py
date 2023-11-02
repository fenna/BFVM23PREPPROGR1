'''Classes and functions that can be used to analyze microarray experiments'''

#some constants to make the code easier to read
PROBE_ID_FIELD = 0
GENE_ID_FIELD = 1
GENE_NAME_FIELD = 3
#some gene name fields contain a ,. With this dirty hack code runs, but part of the gene name
#may be ignored
CHROMOSOME_FIELD = -1
REQUIRED_FIELDS = [PROBE_ID_FIELD, GENE_ID_FIELD, GENE_NAME_FIELD, CHROMOSOME_FIELD]

STRUCTURE_ACRONYM_FIELD = 4
STRUCTURE_ID_FIELD = 0
STRUCTURE_NAME_FIELD = 7

def background_info_generator(background_data, tissue):
    '''
        generator function which reads and processes data from the file containing background data
        Parameters:
            background_data: path to the relevant file
            tissue: the relevant column
    '''
    with open(background_data, encoding = 'us-ascii') as bg_data:
        for line in bg_data:
            p_id, *values = line.strip().split(',')
            yield str(p_id), bool(values[tissue])


def expression_data_generator(expression_data, tissue):
    '''
        generator function which reads and processes data from the file containing expression data
        Parameters:
            annotation_data: path to the relevant file
            tissue: the relevant column
    '''
    with open(expression_data, encoding = 'us-ascii') as ex_data:
        for line in ex_data:
            p_id, *values = line.strip().split(',')
            yield str(p_id), (float(values[tissue]))


def microarray_generator(acronym, ma_annotations, probe_data, background_data, expression_data):
    '''
        generates microarrays for the required acronym
        parameters:
            acronym: the experiment/tissue of interest
            ma_annotions: path to the file containing data about the experiments
            probe_data: path to file containing probe annottions
            background_data: path to file indicating wether or not an expression is
            above its background
            expression_data: path to file containing expression data.

            note that the line in ma_annotations matches the column number in background_data,
                expression_data
    '''
    #get experiment/microarry/tissue information
    with open(ma_annotations, encoding = 'us-ascii') as ann:
        for line_nr, line in enumerate(ann):
            #get only the required line
            fields = line.strip().split(',')
            if fields[STRUCTURE_ACRONYM_FIELD].lower().strip('"') == acronym.lower():
                structure_id = fields[STRUCTURE_ID_FIELD]
                structure_name = fields[STRUCTURE_NAME_FIELD]
                #get the probes, line_nr matches tissue in the probe generator
                probes = probe_generator(probe_data, expression_data, background_data, line_nr)
                return MicroArray(structure_id, acronym, structure_name, probes)


def probe_annotations_generator(probe_data):
    '''generator function which reads the relevant data from a file and returns its contents
        as a key-value pair to be stored in a dictionary
    '''
    with open(probe_data, encoding = 'us-ascii') as p_dat:
        for line in p_dat:
            #ignore the header
            if line.startswith('probe_id'):
                pass
            else:
                p_id, *fields = line.strip().split(',')
                #we don't need all fields. Since lists are convenient but very memory inefficient,
                #we'll use a 'tuple comprehension', which de facto consists of a generator
                #comprehension which is cast to a tuple
                req_fields = tuple((fields[req_field] for req_field in REQUIRED_FIELDS))
#                req_fields = tuple([fields[req_field] for req_field in REQUIRED_FIELDS])
                yield str(p_id), req_fields


def probe_generator(probe_data, expression_data, background_data, region):
    '''In previous demos I used comprehensions to generate probes, which resulted in hard to
        maintain code. Using a generator function fixes the maintainablity issue. I could of
        course wrap this code in a class if a were a real object oriented fanatic

        parameters:
            probe_data: path to the file containing information about the probes (probe_id etc).
            expression_data path to file containing expression data
            background_data:path to file containing background data
            region: the region of interest (column in expression_data and other files)

    '''
    #get the annotations from their file and store those in a dict. Since this is a multi-step
    #process, put it in a separate function. Let's go generator-extreme and use a generator! :))
    # Just use google/duck-duck-go for more
    #information.

    probe_annotations = {p_id:gene_info for p_id, gene_info in probe_annotations_generator(probe_data)}

    #get the expression values of the probes
    probe_expressions = {p_id:values for p_id, values in expression_data_generator(expression_data, region)}

    #the same for the background data
    probe_background_data = {p_id:values for p_id, values in background_info_generator(background_data, region)}

    #create a list of probes.
    for item in probe_annotations.keys():
        yield Probe(item, probe_expressions[item], probe_annotations[item],
                probe_background_data[item])


class InvalidGeneException(Exception):
    '''Exception to indicate something went wrong when creating a gene'''


class InvalidProbeException(Exception):
    '''Exception to indicate something went wrong when creating a probe'''


class MicroArrayCreationException(Exception):
    '''Exception to indicate something went wrong when creating a microarray'''


class Probe():
    '''Models a probe and its expression value on a microarray'''

    #class variable to track the number of probes
    probe_count = 0

    def __init__(self, probe_id, expression_value, gene, above_background):
        '''constructor.
            input: probe_id (str)
                    expression_value (float)
                    gene (tuple consisting of gene_name, gene_id, chromosome). Could of course have
                        been three values, by pylint kept on nagging.
            Please note that requiring all properties to be present at creation time severely limits
            code reuse!
        '''

        #try to set the values, raise a InvalidProbeException when something goes wrong
        try:
            #cast probe_id to string,. Does'nt cause problems if it's a string already and may
            #prevent an exception from occurring
            self.probe_id = int(probe_id)
            #same logic here :)
            self.expression_value = float(expression_value)
            self._gene_id = gene[0]
            self._gene_name = gene[1]
            self._chromosome = gene[3]
            self.is_above_background = bool(above_background)

            #don't forget to up the probe_count!
            Probe.probe_count += 1
        except Exception as oh_ooh:
            raise InvalidProbeException(str(oh_ooh)) from oh_ooh


    @property
    def gene(self):
        '''returns gene information as a tuple'''
        return tuple(self._gene_id, self._gene_name, self._chromosome)


    def __str__(self):
        '''prints probe information as described'''

        return f'''
        Probe id: {self.probe_id}
        Gene id: {self._gene_id}
        Gene name: {self._gene_name}
        Chromosome: {self._chromosome}
        Above background: {self.is_above_background}
        expression: {self.expression_value}
        '''

class MicroArray():
    '''For each experiment a Microarray has been hybridised with an extract of a specific tissue
        or region. When reading the assignment it seems as if Microarray and experiment are used
        interchangeably (e.g. by requiring STructureId etc to be properties of the microarray
        class). This may or may not be what is required. One potential problem may be that it
        assumes that each tisuue/region has only a single associated experiment/copy of the
        microarray. Duplicate experiments will require refactoring the code.
    '''
    experiment_count = 0

    def __init__(self, str_id, str_acronym, str_name, probes):
        '''constructor. All properties of the microarry must be present when created
            probes: should be a list of probes
        '''
        try:
            self.structure_id = str_id
            self.structure_acronym = str_acronym
            self.structure_name = str_name
            self.probes = list(probes)
            MicroArray.experiment_count += 1
        except Exception as oh_ooh:
            #nothing should go wong here
            raise MicroArrayCreationException(str(oh_ooh)) from oh_ooh


    def __str__(self):
        '''
        When printing a microarray this wil be shown as per spec
        '''

        return f'''
        Structure id: {self.structure_id}
        Structure acronym: {self.structure_acronym}
        Structure name: {self.structure_name}
        '''


    def get_probes_above_expression_cutoff(self, cutoff = 0, background = True):
        '''
        return the probes that have an expression value above a certain optional cut off value
        and optionally are above background
        '''

        valid_probes = []
        for probe in self.probes:
            if background:
                if probe.is_above_background and probe.expression_value > cutoff:
                    valid_probes.append(probe)
            else:
                if probe.expression_value > cutoff:
                    valid_probes.append(probe)

        return valid_probes

    def get_probes_above_expression_cutoff_as_set(self, cutoff = 0, background = True):
        '''
        return the probes that have an expression value above a certain optional cut off value
        and optionally are above background
        '''

        valid_probids = set()
        for probe in self.probes:
            if background:
                if probe.is_above_background and probe.expression_value > cutoff:
                    valid_probids.add(probe.probe_id)
            else:
                if probe.expression_value > cutoff:
                    valid_probids.add(probe.probe_id)

        return valid_probids
