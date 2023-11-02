'''
main script for week 4
'''
from assignment04 import microarray_generator


def get_regions():
    '''just a dirty hack for this demo. In reality use argparse or something like that
        to read from the command line
    '''
    return ['LHM', 'PHA']


def get_settings():
    '''just a dirty hack for this demo. In reality use argparse or something like that
        to read from the command line or read from a configuration file
    '''
    return {'expression_data':'../../Data/MicroarrayExpression.csv',
                'probe_data':'../../Data/Probes.csv',
                'annotation_data':'../../Data/SampleAnnot.csv',
                'background_data':'../../Data/PACall.csv',
                'cut_off':15
                }

if __name__ == '__main__':
    settings = get_settings()

    #get the relevant experiments/regions. Normally from the command line
    relevant_regions = get_regions()

    #get the relevant microarrays
    regions = get_regions()
    microarrays = {acronym:microarray_generator(acronym, settings['annotation_data'],
        settings['probe_data'], settings['background_data'], settings['expression_data'])
        for acronym in relevant_regions}
    lhm_probes = microarrays['LHM'].get_probes_above_expression_cutoff_as_set(settings['cut_off'])
    pha_probes = microarrays['PHA'].get_probes_above_expression_cutoff_as_set(settings['cut_off'])

    print(lhm_probes.difference(pha_probes))
    print(pha_probes.difference(lhm_probes))
    print(pha_probes.intersection(lhm_probes))
