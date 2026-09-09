from app.database import SessionLocal
from app.models import Rule


rules = [

    # =========================
    # CHAPTER I - PRELIMINARY
    # =========================

    {
        "rule_number": "1",
        "rule_title": "Short title, application and commencement",
        "chapter": "Chapter I - Preliminary",
        "description": "These rules are called the Legal Metrology (Packaged Commodities) Rules, 2011 and specify their application and commencement.",
        "requirement": "Determine whether the packaged commodity falls within the scope of these rules.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "2",
        "rule_title": "Definitions",
        "chapter": "Chapter I - Preliminary",
        "description": "Defines important terms used in the Legal Metrology (Packaged Commodities) Rules.",
        "requirement": "Interpret packaged commodity, manufacturer, packer, importer, retail package and other defined terms according to the rules.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },


    # =========================
    # CHAPTER II - RETAIL PACKAGES
    # =========================

    {
        "rule_number": "3",
        "rule_title": "Application of the chapter",
        "chapter": "Chapter II - Provisions applicable to packages intended for retail sale",
        "description": "Specifies the applicability of the provisions relating to packages intended for retail sale.",
        "requirement": "Check whether the package is intended for retail sale and apply the applicable requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "4",
        "rule_title": "Specific provisions relating to retail packages",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements applicable to packages intended for retail sale.",
        "requirement": "Retail packages must comply with the applicable provisions of the rules.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "5",
        "rule_title": "Retail packages",
        "chapter": "Chapter II - Retail Packages",
        "description": "Contains provisions relating to packages intended for retail sale.",
        "requirement": "Apply the provisions applicable to retail packages.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "6",
        "rule_title": "Declarations to be made on every package",
        "chapter": "Chapter II - Retail Packages",
        "description": "Specifies the mandatory declarations that are required on packages intended for retail sale.",
        "requirement": "Verify mandatory declarations such as name and address, generic/common name, net quantity, MRP and other applicable declarations.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "7",
        "rule_title": "Principal display panel",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements relating to the principal display panel of a package.",
        "requirement": "Verify that required information is displayed according to the prescribed requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "8",
        "rule_title": "Declaration of quantity",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements relating to declaration of quantity on packages.",
        "requirement": "Verify that net quantity is declared using the prescribed units and manner.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "9",
        "rule_title": "Declaration of dimensions",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements relating to declaration of dimensions where applicable.",
        "requirement": "Verify dimensions and units where declaration of dimensions is applicable.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "10",
        "rule_title": "Declaration of month and year",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements relating to declaration of month and year of manufacture, packing or import where applicable.",
        "requirement": "Verify applicable date declarations.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "11",
        "rule_title": "Name and address of manufacturer, packer and importer",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements for declaring the name and address of the manufacturer, packer or importer.",
        "requirement": "Verify the applicable manufacturer, packer or importer details.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "12",
        "rule_title": "Declaration of quantity",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides additional requirements concerning quantity declarations.",
        "requirement": "Verify that quantity is declared correctly and in the prescribed manner.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "13",
        "rule_title": "General provisions relating to declarations",
        "chapter": "Chapter II - Retail Packages",
        "description": "Contains general provisions concerning declarations on packages.",
        "requirement": "Verify that required declarations are clear, legible and made in the prescribed manner.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "14",
        "rule_title": "Declarations on imported packages",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements applicable to imported packages.",
        "requirement": "Verify applicable declarations for imported packaged commodities.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "15",
        "rule_title": "Permissible variations",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides provisions concerning permissible variations in quantity or measurement.",
        "requirement": "Verify whether observed quantity variation falls within the permitted limits.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "16",
        "rule_title": "Registration of manufacturers and packers",
        "chapter": "Chapter II - Retail Packages",
        "description": "Contains provisions relating to registration requirements where applicable.",
        "requirement": "Verify applicable registration requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "17",
        "rule_title": "Verification of weighing and measuring instruments",
        "chapter": "Chapter II - Retail Packages",
        "description": "Contains requirements concerning weights and measures used in relation to packaged commodities.",
        "requirement": "Verify applicable weighing and measuring requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "18",
        "rule_title": "Compliance requirements",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides requirements relating to compliance with prescribed declarations and measurements.",
        "requirement": "Verify applicable compliance requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "19",
        "rule_title": "Verification requirements",
        "chapter": "Chapter II - Retail Packages",
        "description": "Contains provisions concerning verification of packaged commodities.",
        "requirement": "Verify applicable requirements before determining compliance.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "20",
        "rule_title": "Package marking requirements",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides provisions concerning markings and declarations on packages.",
        "requirement": "Verify required markings and declarations.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "21",
        "rule_title": "Specific requirements",
        "chapter": "Chapter II - Retail Packages",
        "description": "Contains additional requirements applicable to packaged commodities.",
        "requirement": "Verify applicable requirements according to the nature of the commodity.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "22",
        "rule_title": "Compliance with declarations",
        "chapter": "Chapter II - Retail Packages",
        "description": "Provides provisions concerning compliance with declarations made on packages.",
        "requirement": "Verify that declarations correspond with the actual contents and applicable requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "23",
        "rule_title": "Miscellaneous requirements",
        "chapter": "Chapter II - Retail Packages",
        "description": "Contains additional provisions applicable to retail packages.",
        "requirement": "Apply the relevant requirements based on the commodity and package.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },


    # =========================
    # CHAPTER III - WHOLESALE
    # =========================

    {
        "rule_number": "24",
        "rule_title": "Wholesale packages",
        "chapter": "Chapter III - Wholesale Packages",
        "description": "Provides requirements applicable to wholesale packages.",
        "requirement": "Verify declarations and requirements applicable to wholesale packages.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },


    # =========================
    # CHAPTER IV - EXPORT
    # =========================

    {
        "rule_number": "25",
        "rule_title": "Export packages",
        "chapter": "Chapter IV - Export",
        "description": "Provides provisions applicable to packages intended for export.",
        "requirement": "Verify requirements applicable to export packages.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },


    # =========================
    # CHAPTER V - EXEMPTIONS
    # =========================

    {
        "rule_number": "26",
        "rule_title": "Exemptions",
        "chapter": "Chapter V - Exemptions",
        "description": "Specifies categories of packaged commodities that are exempted from specified provisions subject to the conditions in the rule.",
        "requirement": "Before declaring a package non-compliant, check whether the commodity qualifies for an exemption under Rule 26.",
        "is_exempted_under_rule_26": True,
        "is_active": True
    },


    # =========================
    # CHAPTER VI - REGISTRATION
    # =========================

    {
        "rule_number": "27",
        "rule_title": "Registration of manufacturers and packers",
        "chapter": "Chapter VI - Registration",
        "description": "Provides requirements relating to registration of manufacturers and packers of packaged commodities.",
        "requirement": "Verify applicable registration requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "28",
        "rule_title": "Registration requirements",
        "chapter": "Chapter VI - Registration",
        "description": "Provides additional provisions relating to registration.",
        "requirement": "Verify whether applicable registration requirements have been fulfilled.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "29",
        "rule_title": "Registration records",
        "chapter": "Chapter VI - Registration",
        "description": "Contains provisions relating to registration records and related requirements.",
        "requirement": "Maintain and verify applicable registration information.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },


    # =========================
    # CHAPTER VII - ADMINISTRATION
    # =========================

    {
        "rule_number": "30",
        "rule_title": "Offences and penalties",
        "chapter": "Chapter VII - Administration",
        "description": "Contains administrative provisions concerning violations of the rules.",
        "requirement": "Record applicable non-compliance and determine the relevant regulatory action.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "31",
        "rule_title": "Enforcement",
        "chapter": "Chapter VII - Administration",
        "description": "Contains provisions concerning enforcement of the rules.",
        "requirement": "Apply applicable enforcement provisions.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "32",
        "rule_title": "Power to inspect",
        "chapter": "Chapter VII - Administration",
        "description": "Contains provisions concerning inspection and enforcement.",
        "requirement": "Apply the prescribed inspection requirements.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "32A",
        "rule_title": "Additional administrative provision",
        "chapter": "Chapter VII - Administration",
        "description": "Contains an additional administrative provision introduced through amendment.",
        "requirement": "Apply the requirement where applicable.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "33",
        "rule_title": "General provisions",
        "chapter": "Chapter VII - Administration",
        "description": "Contains general administrative provisions.",
        "requirement": "Apply the applicable general provisions.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    },

    {
        "rule_number": "34",
        "rule_title": "Repeal and saving",
        "chapter": "Chapter VII - Administration",
        "description": "Contains provisions concerning repeal and saving.",
        "requirement": "Apply the applicable repeal and saving provisions.",
        "is_exempted_under_rule_26": False,
        "is_active": True
    }
]


def seed_rules():

    db = SessionLocal()

    try:

        inserted = 0
        skipped = 0

        for rule_data in rules:

            # Check whether rule already exists
            existing_rule = db.query(Rule).filter(
                Rule.rule_number == rule_data["rule_number"]
            ).first()

            if existing_rule:
                print(
                    f"Rule {rule_data['rule_number']} already exists - skipped"
                )
                skipped += 1
                continue

            rule = Rule(**rule_data)

            db.add(rule)
            inserted += 1

        db.commit()

        print("\n==============================")
        print("RULE SEEDING COMPLETED")
        print("==============================")
        print("Rules inserted :", inserted)
        print("Rules skipped  :", skipped)

    except Exception as e:

        db.rollback()

        print("Error while inserting rules:")
        print(e)

    finally:

        db.close()


if __name__ == "__main__":
    seed_rules()