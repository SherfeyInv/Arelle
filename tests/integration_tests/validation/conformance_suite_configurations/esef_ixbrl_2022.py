from pathlib import PurePath
from tests.integration_tests.validation.conformance_suite_config import ConformanceSuiteConfig

config = ConformanceSuiteConfig(
    args=[
        '--disclosureSystem', 'esef',
        '--formula', 'run',
        '--plugins', 'validate/ESEF_2022',
    ],
    expected_failure_ids=frozenset([
        # The following test cases fail because of the `tech_duplicated_facts1` formula which fires
        # incorrectly because it does not take into account the language attribute on the fact.
        # A fact can not be a duplicate fact if the language attributes are different.
        'inline_xbrl/RTS_Annex_IV_Par_12_G2-2-4/TC5_valid'
    ]),
    file='esef_conformance_suite_2022/index_inline_xbrl.xml',
    info_url='https://www.esma.europa.eu/document/conformance-suite-2022',
    local_filepath='esef_conformance_suite_2022.zip',
    name=PurePath(__file__).stem,
    public_download_url='https://www.esma.europa.eu/sites/default/files/library/esef_conformance_suite_2022.zip',
)
