import os, re, time, datetime, csv, sys
import rethinkdb as r
from Bio import SeqIO
from vdb_upload import vdb_upload
from vdb_upload import parser

class Zika_vdb_upload(vdb_upload):

    def __init__(self,  fasta_fields, fasta_fname, database, virus, source, overwrite, locus=None, vsubtype=None, authors=None, path=None, auth_key=None):
        '''
        :param fasta_fields: Dictionary defining position in fasta field to be included in database
        '''
        vdb_upload.__init__(self, fasta_fields, fasta_fname, database, virus, source, overwrite, locus, vsubtype, authors, path, auth_key)
        self.virus_optional_fields = ['division', 'location']
        self.updateable_virus_fields = ['date', 'country', 'division', 'location', 'virus']

if __name__=="__main__":
    args = parser.parse_args()
    fasta_fields = {0:'accession', 2:'strain', 4:'date', 6:'country'}
    # 0        1          2      3  4          5     6
    #>KU501216|Zika_virus|103344|NA|2015_12_01|Human|Guatemala
    run = Zika_vdb_upload(fasta_fields, fasta_fname=args.fname, database=args.database, virus=args.virus, source=args.source, overwrite=args.overwrite, locus=args.locus, vsubtype=args.subtype, authors=args.authors, path=args.path)
    run.upload()