"""
Install tools needed to run biokepler demo workflows.
More information of biokepler can be found at www.biokepler.org
Jianwu Wang (jianwu@sdsc.edu)
"""
import os
import re

from fabric.api import *
from fabric.contrib.files import *
import yaml

from shared import (_remote_fetch,
                    _if_not_installed, _make_tmp_dir,
                    _get_install, _get_install_local, _make_copy, _configure_make,
                    _java_install, _python_cmd,
                    _symlinked_java_version_dir, _fetch_and_unpack, _python_make,
                    _get_lib_dir, _get_include_dir)
from cloudbio.custom import shared, versioncheck

from cloudbio import libraries
from cloudbio.flavor.config import get_config_file

def install_biokepler(env):
    url = "http://www.biokepler.org/files/downloads/biokepler-1.0.deb"
    tool = url[url.rfind('/')+1:]
    _download_install_deb_pkg(env, url, tool)
    """todo: add kepler.sh link to desktop"""

def install_qiime(env):
    env.safe_sudo("apt-get install -y --force-yes qiime")

@_if_not_installed("mothur")
def install_mothur(env):
    url = "https://launchpad.net/~tbooth/+archive/ppa1/+build/3486018/+files/mothur_1.25.0~repack-lucid3_amd64.deb"
    tool = url[url.rfind('/')+1:]
    _download_install_deb_pkg(env, url, tool)

@_if_not_installed("ssake")
def install_ssake(env):
    url = "http://ubuntu.wikimedia.org/ubuntu//pool/universe/s/ssake/ssake_3.4-1_all.deb" 
    tool = url[url.rfind('/')+1:]
    _download_install_deb_pkg(env, url, tool)

@_if_not_installed("breakdancer")
def install_breakdancer(env):
    """Useful executables from UCSC.
    todo: install from source to handle 32bit and get more programs
    http://hgdownload.cse.ucsc.edu/admin/jksrc.zip
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "breakdancer")
"""    with _make_tmp_dir() as work_dir:
        with cd(work_dir):
            _remote_fetch(env, url + tool + ".tar.gz")
            env.safe_sudo("tar -xzvpf %s.tar.gz -C /usr/" % tool)
"""

def install_cd_hit(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "cd-hit")

def install_cd_hit_454(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "cd-hit-454")

def install_cd_hit_est(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "cd-hit-est")

@_if_not_installed("metagene.pl")
def install_metagene(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "metagene")

@_if_not_installed("fraggene_scan.pl")
def install_fraggene_scan(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "fraggene_scan")

#@_if_not_installed("orf_finder")
def install_orf_finder(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    print("start install orf_finder")
    _install_tar_ball(env, url, "orf_finder")

@_if_not_installed("qc_filter_fastq.pl")
def install_qc_filter_fastq(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "qc_filter_fastq")

@_if_not_installed("qc_filter.pl")
def install_qc_filter(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    env.safe_sudo("cpanm install Bio::SeqIO") 
    env.safe_sudo("rm -rf .cpanm")
    _install_tar_ball(env, url, "qc_filter")

@_if_not_installed("DynamicTrim.pl")
def install_trim(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "trim")

@_if_not_installed("fastq2fasta")
def install_fastq2fasta(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "fastq2fasta")

@_if_not_installed("soap")
def install_soap(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "soap")

@_if_not_installed("SOAPdenovo127mer")
def install_soapdenovo(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "soapdenovo")

@_if_not_installed("faa_stat.pl")
def install_faa_stat(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "faa_stat")

@_if_not_installed("fna_stat.pl")
def install_fna_stat(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "fna_stat")

@_if_not_installed("tRNAscan-SE.pl")
def install_trnascan_se(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "tRNAscan-SE")

@_if_not_installed("blast_rRNA.pl")
def install_blast_rrna(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "blast_rRNA")

@_if_not_installed("blast_rRNA.pl")
def install_blastrrna(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "blast_rRNA")

@_if_not_installed("hmm_rRNA.pl")
def install_hmm_rrna(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_ball(env, url, "hmm_rRNA")

#@_if_not_installed("cdd_ann_parse_post_COG.pl")
def install_cog(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    tool = "COG"
    _install_tar_and_db(env, url, tool)

@_if_not_installed("cdd_ann_parse_post_KOG.pl")
def install_kog(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    tool = "KOG"
    _install_tar_and_db(env, url, tool)

def install_pfam(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_and_db(env, url, "PFAM")

@_if_not_installed("kegg.pl")
def install_kegg(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_and_db(env, url, "KEGG")

@_if_not_installed("hmmsearch.pl")
def install_tigrfam(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_and_db(env, url, "TIGRFAM")

@_if_not_installed("cdd_ann_parse_post_PRK.pl")
def install_prk(env):
    """Install tools for biokepler project.
    """
    url = "http://weizhong-lab.ucsd.edu/bio-kepler/"
    _install_tar_and_db(env, url, "PRK")

def _download_install_deb_pkg(env, url, tool):
    with _make_tmp_dir() as work_dir:
        with cd(work_dir):
            _remote_fetch(env, url)
            env.safe_sudo("dpkg -i " + tool);


def _install_tar_ball(env, url, tool):
    install_dir = shared._get_bin_dir(env)
    install_dir_parent = os.path.abspath(os.path.join(install_dir, os.pardir))
    with _make_tmp_dir() as work_dir:
        with cd(work_dir):
            _remote_fetch(env, url + tool + ".tar.gz")
            #env.safe_sudo("tar -xzvpf %s.tar.gz -C %s" % (tool, install_dir))
            #env.safe_sudo("chown -R %s '%s'" % (env.user, install_dir_parent))
            #env.safe_sudo("chgrp -R %s '%s'" % (env.user, install_dir_parent))
            env.safe_sudo("tar -xzvpf %s.tar.gz -C %s" % (tool, install_dir_parent))
            env.safe_sudo("chown -R %s:%s '%s'" % (env.user, env.user, install_dir))
            #env.safe_sudo("chgrp -R %s '%s'" % (env.user, install_dir))

def _install_tar_and_db(env, url, tool):
    install_dir = shared._get_bin_dir(env)
    install_dir_parent = os.path.abspath(os.path.join(install_dir, os.pardir))
    with _make_tmp_dir() as work_dir:
        with cd(work_dir):
            _remote_fetch(env, url + tool + ".tar.gz")
            #env.safe_sudo("tar -xzvpf %s.tar.gz -C %s" % (tool, install_dir))
            #env.safe_sudo("chown -R %s '%s'" % (env.user, install_dir_parent))
            #env.safe_sudo("chgrp -R %s '%s'" % (env.user, install_dir_parent))
            env.safe_sudo("tar -xzvpf %s.tar.gz -C %s" % (tool, install_dir_parent))
            env.safe_sudo("chown -R %s:%s '%s'" % (env.user, env.user, install_dir))
            #env.safe_sudo("chgrp -R %s '%s'" % (env.user, install_dir))
            _remote_fetch(env, url + tool + "_db.tar.gz")
            #env.safe_sudo("tar -xzvpf %s_db.tar.gz -C %s" % (tool, install_dir))
            #env.safe_sudo("chown -R %s '%s'" % (env.user, install_dir_parent))
            #env.safe_sudo("chgrp -R %s '%s'" % (env.user, install_dir_parent))
            env.safe_sudo("tar -xzvpf %s_db.tar.gz -C %s" % (tool, install_dir_parent))
            env.safe_sudo("chown -R %s:%s '%s'" % (env.user, env.user, install_dir_parent + '/reference_db'))
            #env.safe_sudo("chgrp -R %s '%s'" % (env.user, install_dir_parent + '/reference_db'))
