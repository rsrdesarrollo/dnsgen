# python3

import os
import sys

import click

from . import dnsgen
from dnsgen.dnsgen import GRP_INCREASE, GRP_DECREASE, GRP_INSERT, GRP_PREFIX, GRP_SUFFIX, GRP_REPLACE


@click.command()
@click.option('-l', '--wordlen', default=6, 
                help='Min length of custom words extracted from domains.', 
                required=False, type=click.IntRange(1, 100))
@click.option('-w', '--wordlist', default=None, help='Path to custom wordlist.', 
                type=click.Path(exists=True, readable=True), required=False)
@click.option('-f', '--fast', default=None, help='Fast generation.', 
                is_flag=True, required=False)
@click.option('-p', '--processors', default=["all"], help='List of processors to use.', 
                multiple=True, required=False, type=click.Choice([
                    GRP_INCREASE, GRP_DECREASE, GRP_INSERT, GRP_PREFIX, GRP_SUFFIX, GRP_REPLACE, "all"
                ], case_sensitive=False))
@click.argument('filename', required=True, type=click.File(mode='r'))
def main(wordlen, wordlist, filename, fast, processors):
    # read the input
    domains = filename.read().splitlines()

    for r in dnsgen.generate(domains, wordlist, wordlen, fast=fast, processors=processors):
        click.echo(r)
